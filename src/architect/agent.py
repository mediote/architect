from typing import Dict, Any, Optional
import time
from .memory import Memory
from .weather import OpenWeatherClient

class ClimateAgent:
    """Agent responsible for perceiving climate data and producing a response."""

    def __init__(self, weather_client: OpenWeatherClient, memory: Optional[Memory] = None) -> None:
        self.weather_client = weather_client
        self.memory = memory or Memory()

    def perceive(self, city: str) -> Dict[str, Any]:
        data = self.weather_client.fetch_city_weather(city)
        self.memory.add({"timestamp": time.time(), "city": city, "data": data})
        return data

    @staticmethod
    def decide_response(city: str, data: Dict[str, Any]) -> str:
        main = data.get("main", {})
        weather = (data.get("weather") or [{}])[0]
        temp = main.get("temp", "?")
        desc = weather.get("description", "?")
        return f"Clima em {city}: {temp}°C, {desc}"

    def act(self, city: str) -> str:
        data = self.perceive(city)
        return self.decide_response(city, data)
