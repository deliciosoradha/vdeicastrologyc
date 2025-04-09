from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class BirthData(BaseModel):
    name: str
    birth_date: datetime
    birth_time: str
    birth_place: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class AstrologyResponse(BaseModel):
    rashi_chart: Dict[str, str]
    current_transits: Dict[str, str]
    nakshatra: str
    dasha: str
    antardasha: str
    planetary_positions: Dict[str, str]
    aspects: List[Dict[str, str]]
    vimshottari_dasha: Dict[str, str]
    predictions: List[str]

class PDFRequest(BaseModel):
    birth_data: BirthData
    astrology_data: AstrologyResponse
    include_educational_content: bool = True

class ChatMessage(BaseModel):
    user_id: str
    message: str
    context: Optional[Dict] = None

class PaymentRequest(BaseModel):
    user_id: str
    amount: float
    currency: str = "USD"
    description: str = "Vedic Astrology Report"
