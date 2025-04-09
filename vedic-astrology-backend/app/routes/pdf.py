from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from app.schemas import PDFRequest
from app.services.pdf_generator import PDFGenerator
from typing import Dict
import os

router = APIRouter(prefix="/api/pdf", tags=["PDF Generation"])

@router.post("/generate")
async def generate_pdf(
    request: PDFRequest,
    pdf_service: PDFGenerator = Depends()
) -> Dict[str, str]:
    """
    Generate a PDF report from astrology data
    Returns preview HTML and PDF download URL
    """
    try:
        pdf_path, html_content = pdf_service.generate_report(request)
        return {
            "preview_html": html_content,
            "pdf_url": f"/download/{os.path.basename(pdf_path)}",
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"PDF generation failed: {str(e)}"
        )

@router.get("/download/{filename}")
async def download_pdf(filename: str):
    """Endpoint to download generated PDF"""
    pdf_path = os.path.join("reports", filename)
    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=404, detail="PDF not found")
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"vedic_report_{filename}"
    )
