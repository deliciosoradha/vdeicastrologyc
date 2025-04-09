from fastapi import APIRouter, Depends, HTTPException
from app.schemas import BirthData, AstrologyResponse
from app.services.astrology import AstrologyService
from typing import Optional

router = APIRouter(prefix="/api/astrology", tags=["Astrology"])

@router.post("/chart", response_model=AstrologyResponse)
async def get_vedic_chart(
    birth_data: BirthData,
    astrology_service: AstrologyService = Depends()
):
    """
    Get Vedic astrology chart data including:
    - Rashi chart
    - Current transits
    - Nakshatras and Dashas
    - Planetary positions
    """
    try:
        return await astrology_service.get_vedic_chart(birth_data)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating Vedic chart: {str(e)}"
        )

@router.get("/interpretation/{chart_id}")
async def get_interpretation(chart_id: str):
    """
    Get interpretation for a specific chart
    """
    # TODO: Implement interpretation logic
    return {"message": "Interpretation endpoint", "chart_id": chart_id}
