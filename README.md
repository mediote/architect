# Architect – Climate Agent

A minimal **memory-augmented climate agent** built with **FastAPI**. The agent fetches real-time weather data from OpenWeather, stores recent perceptions in memory, and exposes an HTTP API.

## Features
- Memory-augmented agent loop (perceive → decide → act)
- OpenWeather API integration
- FastAPI service with JSON endpoints
- Simple bounded in-memory event store

## Requirements
- Python 3.9+
- OpenWeather API key

## Installation
```bash
pip install fastapi uvicorn requests pydantic
```

## Configuration
Set your OpenWeather API key:
```bash
export OPENWEATHER_API_KEY=your_api_key_here
```

## Running
```bash
uvicorn src.agent_clima:app --reload
```

## API
### POST /climate
Request:
```json
{ "city": "São Paulo" }
```
Response:
```json
{ "response": "Clima em São Paulo: 22°C, céu limpo" }
```

### GET /memory
Returns recent weather perceptions stored by the agent.

## Project Structure
```
src/
  agent_clima.py   # Climate agent and FastAPI app
```

## License
MIT
