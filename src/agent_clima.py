"""
Climate Agent using a Memory-Augmented Framework (MAF) with FastAPI.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import os
import time
import requests


class Memory:
    """Bounded in-memory event store."""

    def __init__(self, max_size: int = 100) -> None:
        self.max_size = max_size
        self._events: List[Dict[str, Any]] = []

    def add(self, event: Dict[str, Any]) -> None:
        self._events.append(event)
        if len(self._events) > self.max_size:
            self._events.pop(0)

    def all(self) -> List[Dict[str, Any]]:
        return list(self._events)


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


# ===== FASTAPI =====

class CityRequest(BaseModel):
    city: str


class ClimateResponse(BaseModel):
    response: str


def create_app() -> FastAPI:
    app = FastAPI(title="Climate Agent MAF")
    api_key = os.getenv("OPENWEATHER_API_KEY", "")
    weather_client = OpenWeatherClient(api_key=api_key)
    agent = ClimateAgent(weather_client=weather_client)

    @app.post("/climate", response_model=ClimateResponse)
    def get_climate(req: CityRequest) -> ClimateResponse:
        try:
            return ClimateResponse(response=agent.act(req.city))
        except Exception as exc:  # pragma: no cover
            raise HTTPException(status_code=500, detail=str(exc))

    @app.get("/memory")
    def get_memory() -> List[Dict[str, Any]]:
        return agent.memory.all()

    return app


app = create_app()
