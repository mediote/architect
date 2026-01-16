from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config.settings import settings
from architect.weather import OpenWeatherClient
from architect.agent import ClimateAgent

class CityRequest(BaseModel):
    city: str

class ClimateResponse(BaseModel):
    response: str


def create_app() -> FastAPI:
    app = FastAPI(title="Climate Agent MAF")
    weather_client = OpenWeatherClient(api_key=settings.openweather_api_key)
    agent = ClimateAgent(weather_client=weather_client)

    @app.post("/climate", response_model=ClimateResponse)
    def get_climate(req: CityRequest) -> ClimateResponse:
        try:
            return ClimateResponse(response=agent.act(req.city))
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @app.get("/memory")
    def get_memory():
        return agent.memory.all()

    return app

app = create_app()
