from typing import Dict, Any, Optional
import time
from .memory import Memory
from .weather import OpenWeatherClient
from .formatter import ClimateResponseFormatter


class ClimateAgent:
    """Agent responsible for retrieving climate data and generating human-readable responses."""

    def __init__(
        self,
        weather_client: OpenWeatherClient,
        memory: Optional[Memory] = None,
        formatter: Optional[ClimateResponseFormatter] = None,
    ) -> None:
        self.weather_client = weather_client
        self.memory = memory or Memory()
        self.formatter = formatter or ClimateResponseFormatter()

    def fetch_weather(self, city: str) -> Dict[str, Any]:
        """Fetch and store raw weather data for a given city."""
        try:
            data: Dict[str, Any] = self.weather_client.fetch_city_weather(city)
        except Exception as exc:
            data = {"error": str(exc)}
        self._store_memory(city, data)
        return data

    def generate_response(self, city: str, data: Dict[str, Any]) -> str:
        """Generate a user-facing response from raw weather data."""
        return self.formatter.format(city, data)

    def act(self, city: str) -> str:
        """High-level execution: fetch weather data and generate a response."""
        data = self.fetch_weather(city)
        return self.generate_response(city, data)

    def _store_memory(self, city: str, data: Dict[str, Any]) -> None:
        self.memory.add({"timestamp": time.time(), "city": city, "data": data})
