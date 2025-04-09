import requests
from typing import Dict, Any
from app.schemas import BirthData, AstrologyResponse
import os

class AstrologyService:
    def __init__(self):
        self.api_url = os.getenv("ASTROLOGY_API_URL", "https://api.vedicastrology.com/v1")
        self.api_key = os.getenv("ASTROLOGY_API_KEY")

    async def get_vedic_chart(self, birth_data: BirthData) -> AstrologyResponse:
        """Get Vedic astrology chart data from external API"""
        payload = {
            "name": birth_data.name,
            "birth_date": birth_data.birth_date.isoformat(),
            "birth_time": birth_data.birth_time,
            "latitude": birth_data.latitude,
            "longitude": birth_data.longitude
        }

        try:
            response = requests.post(
                f"{self.api_url}/charts",
                json=payload,
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return self._parse_response(response.json())
        except Exception as e:
            raise Exception(f"Astrology API error: {str(e)}")

    def _parse_response(self, data: Dict[str, Any]) -> AstrologyResponse:
        """Parse API response into our schema"""
        return AstrologyResponse(
            rashi_chart=data.get("rashi_chart", {}),
            current_transits=data.get("current_transits", {}),
            nakshatra=data.get("nakshatra", ""),
            dasha=data.get("dasha", ""),
            antardasha=data.get("antardasha", ""),
            planetary_positions=data.get("planetary_positions", {}),
            aspects=data.get("aspects", []),
            vimshottari_dasha=data.get("vimshottari_dasha", {}),
            predictions=data.get("predictions", [])
        )
