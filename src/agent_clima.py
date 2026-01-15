"""
Climate Agent using a simple Memory-Augmented Framework (MAF) and FastAPI.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import os
import time
import requests

# ===== MAF CORE =====
class Memory:
    """Simple bounded in-memory event store."""

    def __init__(self, max_size: int = 100) -> None:
        self.max_size = max_size
        self._events: List[Dict[str, Any]] = []

    def add(self, data: Dict[str, Any]) -> None:
        self._events.append(data)
        if len(self._events) > self.max_size:
            self._events.pop(0)

    def all(self) -> List[Dict[str, Any]]:
        return list(self._events)


class ClimateAgent:
    """Agent responsible for perceiving climate data and producing a response."""

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, city: str, api_key: str, memory: Memory | None = None) -> None:
        self.city = city
        self.api_key = api_key
        self.memory = memory or Memory()
        self._session = requests.Session()

    def perceive(self) -> Dict[str, Any]:
        if not self.api_key:
            raise RuntimeError("OPENWEATHER_API_KEY is not configured")

        params = {
            "q": self.city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "pt_br",
        }
        response = self._session.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        event = {"timestamp": time.time(), "data": data}
        self.memory.add(event)
        return data

    def decide(self, data: Dict[str, Any]) -> str:
        main = data.get("main", {})
        weather = (data.get("weather") or [{}])[0]
        temp = main.get("temp", "?")
        desc = weather.get("description", "?")
        return f"Clima em {self.city}: {temp}°C, {desc}"

    def act(self) -> str:
        data = self.perceive()
        return self.decide(data)


# ===== FASTAPI =====
app = FastAPI(title="Climate Agent MAF")
API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
agent = ClimateAgent(city="Sao Paulo", api_key=API_KEY)


class CityRequest(BaseModel):
    city: str


@app.get("/climate")
def get_climate() -> Dict[str, str]:
    try:
        return {"response": agent.act()}
    except Exception as exc:  # pragma: no cover - API safety
        raise HTTPException(status_code=500, detail=str(exc))


@app.get("/memory")
def get_memory() -> List[Dict[str, Any]]:
    return agent.memory.all()
