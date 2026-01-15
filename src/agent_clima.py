"""
Agente de Clima usando um modelo simples de MAF (Multi-Agent Framework).
Este agente consulta uma API publica de clima e responde com a previsao atual.
"""

import requests

class ClimateAgent:
    def __init__(self, city: str, api_key: str):
        self.city = city
        self.api_key = api_key

    def perceive(self):
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={self.city}&appid={self.api_key}&units=metric&lang=pt_br"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    def decide(self, data: dict) -> str:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"Clima atual em {self.city}: {temp}°C, {desc}."

    def act(self) -> str:
        data = self.perceive()
        return self.decide(data)


if __name__ == "__main__":
    # Exemplo de uso
    import os
    api_key = os.getenv("OPENWEATHER_API_KEY")
    agent = ClimateAgent("Sao Paulo", api_key)
    print(agent.act())
