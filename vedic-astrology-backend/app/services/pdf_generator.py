from weasyprint import HTML
from app.schemas import PDFRequest
import os
from datetime import datetime
from typing import Tuple
import tempfile

class PDFGenerator:
    def __init__(self):
        self.output_dir = os.getenv("PDF_OUTPUT_DIR", "reports")
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_report(self, request: PDFRequest) -> Tuple[str, str]:
        """Generate a PDF report from astrology data"""
        try:
            # Generate HTML content
            html_content = self._generate_html(request)
            
            # Create PDF
            pdf_filename = f"vedic_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            pdf_path = os.path.join(self.output_dir, pdf_filename)
            
            HTML(string=html_content).write_pdf(pdf_path)
            
            return pdf_path, html_content
        except Exception as e:
            raise Exception(f"PDF generation failed: {str(e)}")

    def _generate_html(self, request: PDFRequest) -> str:
        """Generate HTML content for the PDF"""
        # Basic HTML template - can be expanded with more detailed content
        return f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial; margin: 2cm; }}
                    h1 {{ color: #4a2c82; }}
                    .section {{ margin-bottom: 20px; }}
                </style>
            </head>
            <body>
                <h1>Vedic Astrology Report for {request.birth_data.name}</h1>
                
                <div class="section">
                    <h2>Birth Details</h2>
                    <p>Date: {request.birth_data.birth_date}</p>
                    <p>Time: {request.birth_data.birth_time}</p>
                    <p>Place: {request.birth_data.birth_place}</p>
                </div>
                
                <div class="section">
                    <h2>Planetary Positions</h2>
                    {self._format_planetary_positions(request.astrology_data.planetary_positions)}
                </div>
                
                {self._generate_educational_content() if request.include_educational_content else ''}
            </body>
        </html>
        """

    def _format_planetary_positions(self, positions: dict) -> str:
        """Format planetary positions as HTML"""
        return "<ul>" + "".join(
            f"<li><strong>{planet}:</strong> {position}</li>"
            for planet, position in positions.items()
        ) + "</ul>"

    def _generate_educational_content(self) -> str:
        """Generate educational content about Vedic astrology"""
        return """
        <div class="section">
            <h2>About Vedic Astrology</h2>
            <p>Vedic astrology, also known as Jyotish, is an ancient Indian system...</p>
        </div>
        """
