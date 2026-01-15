# Refatorado: Agent de Clima com MAF + FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import requests, time, os
from typing import List, Dict, Any

# ===== MAF CORE =====
class Memory:
    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self.events: List[Dict[str, Any]] = []

    def add(self, data: Dict[str, Any]):
        self.events.append(data)
        if len(self.events) > self.max_size:
            self.events.pop(0)

    def all(self):
        return self.events

class ClimateAgent:
    def __init__(self, city: str, api_key: str):
        self.city = city
        self.api_key = api_key
        self.memory = Memory()

    def perceive(self) -> Dict[str, Any]:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric&lang=pt_br"
        data = requests.get(url, timeout=10).json()
        event = {"timestamp": time.time(), "data": data}
        self.memory.add(event)
        return data

    def decide(self, data: Dict[str, Any]) -> str:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"Clima em {self.city}: {temp}°C, {desc}"  

    def act(self) -> str:
        return self.decide(self.perceive())

# ===== FASTAPI =====
app = FastAPI(title="Climate Agent MAF")
API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
agent = ClimateAgent("Sao Paulo", API_KEY)

class CityRequest(BaseModel):
    city: str

@app.get("/climate")
def get_climate():
    return {"response": agent.act()}

@app.get("/memory")
def get_memory():
    return agent.memory.all()
