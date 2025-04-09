from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/api/form", tags=["Form Submission"])

class BirthData(BaseModel):
    name: str
    birth_date: datetime
    birth_time: str
    birth_place: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

@router.post("/submit")
async def submit_birth_data(data: BirthData):
    """
    Endpoint to receive birth data from the frontend
    """
    try:
        # Validate and process the data
        if not data.birth_time or not data.birth_place:
            raise HTTPException(
                status_code=400,
                detail="Birth time and place are required"
            )

        # TODO: Add coordinates lookup if not provided
        if not data.latitude or not data.longitude:
            # Placeholder for geocoding service
            pass

        return {
            "status": "success",
            "message": "Birth data received successfully",
            "data": data.dict()
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing birth data: {str(e)}"
        )
