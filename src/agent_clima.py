"""
Agente de Clima usando um MAF (Multi-Agent Framework) simplificado.
Inclui percepcao, decisao, acao e memoria interna para historico de estados.
"""

import requests
import time
from typing import Dict, List, Any


class AgentMemory:
    """Memoria simples baseada em historico temporal."""

    def __init__(self, max_size: int = 50):
        self.max_size = max_size
        self._events: List[Dict[str, Any]] = []

    def add(self, event: Dict[str, Any]) -> None:
        self._events.append(event)
        if len(self._events) > self.max_size:
            self._events.pop(0)

    def last(self) -> Dict[str, Any] | None:
        return self._events[-1] if self._events else None

    def all(self) -> List[Dict[str, Any]]:
        return list(self._events)


class ClimateAgent:
    """Agente autonomo de clima seguindo o ciclo MAF: perceber, decidir, agir."""

    def __init__(self, city: str, api_key: str, memory_size: int = 20):
        self.city = city
        self.api_key = api_key
        self.memory = AgentMemory(memory_size)

    # === PERCEPCAO ===
    def perceive(self) -> Dict[str, Any]:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={self.city}&appid={self.api_key}&units=metric&lang=pt_br"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        percept = {
            "timestamp": time.time(),
            "raw": data,
        }
        self.memory.add(percept)
        return data

    # === DECISAO ===
    def decide(self, data: Dict[str, Any]) -> str:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        trend = "estavel"
        last = self.memory.last()
        if last and "raw" in last:
            try:
                last_temp = last["raw"]["main"]["temp"]
                if temp > last_temp:
                    trend = "aquecendo"
                elif temp < last_temp:
                    trend = "esfriando"
            except Exception:
                pass

        return (
            f"Clima atual em {self.city}: {temp}°C, {desc}, "
            f"umidade {humidity}%. Tendencia: {trend}."
        )

    # === ACAO ===
    def act(self) -> str:
        data = self.perceive()
        decision = self.decide(data)
        return decision

    # === METODOS AUXILIARES ===
    def recall_history(self) -> List[Dict[str, Any]]:
        """Retorna o historico completo da memoria do agente."""
        return self.memory.all()


if __name__ == "__main__":
    # Exemplo de uso
    import os

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("Defina a variavel OPENWEATHER_API_KEY")

    agent = ClimateAgent("Sao Paulo", api_key)
    print(agent.act())
