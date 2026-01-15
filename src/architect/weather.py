from typing import Dict, Any, Optional
import requests

class OpenWeatherClient:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str, session: Optional[requests.Session] = None) -> None:
        if not api_key:
            raise RuntimeError("OPENWEATHER_API_KEY is not configured")
        self.api_key = api_key
        self.session = session or requests.Session()

    def fetch_city_weather(self, city: str) -> Dict[str, Any]:
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "pt_br",
        }
        response = self.session.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
