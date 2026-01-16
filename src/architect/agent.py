from typing import Dict, Any, Optional
import time
from .memory import Memory
from .weather import OpenWeatherClient


class ClimateAgent:
    """Agent responsible for retrieving climate data and generating human-readable responses."""

    def __init__(self, weather_client: OpenWeatherClient, memory: Optional[Memory] = None) -> None:
        self.weather_client: OpenWeatherClient = weather_client
        self.memory: Memory = memory or Memory()

    def perceive(self, city: str) -> Dict[str, Any]:
        """Fetch and store raw weather data for a given city."""
        try:
            data: Dict[str, Any] = self.weather_client.fetch_city_weather(city)
        except Exception as exc:
            data = {"error": str(exc)}
        self._store_memory(city, data)
        return data

    @staticmethod
    def decide_response(city: str, data: Dict[str, Any]) -> str:
        """Convert raw weather data into a user-facing string."""
        if "error" in data:
            return f"Erro ao obter clima para {city}: {data['error']}"

        main: Dict[str, Any] = data.get("main", {})
        weather: Dict[str, Any] = (data.get("weather") or [{}])[0]
        temperature = main.get("temp", "?")
        description = weather.get("description", "?")
        return f"Clima em {city}: {temperature}°C, {description}"

    def act(self, city: str) -> str:
        """High-level execution: perceive the environment and act on it."""
        data = self.perceive(city)
        return self.decide_response(city, data)

    def _store_memory(self, city: str, data: Dict[str, Any]) -> None:
        self.memory.add({"timestamp": time.time(), "city": city, "data": data})
