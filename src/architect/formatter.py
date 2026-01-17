from typing import Dict, Any


class ClimateResponseFormatter:
    """Formats raw weather data into human-readable responses."""

    def format(self, city: str, data: Dict[str, Any]) -> str:
        if "error" in data:
            return f"Erro ao obter clima para {city}: {data['error']}"

        main: Dict[str, Any] = data.get("main", {})
        weather: Dict[str, Any] = (data.get("weather") or [{}])[0]
        temperature = main.get("temp", "?")
        description = weather.get("description", "?")
        return f"Clima em {city}: {temperature}°C, {description}"
