# Architect – Climate Agent

Architect is a minimal **memory-augmented AI agent** implemented as a **FastAPI** service.
It demonstrates a clean agent loop (**perceive → decide → act**) combined with an external data source (OpenWeather) and short-term memory.

## Overview
The agent receives a city name, fetches real-time climate data from the OpenWeather API, stores recent perceptions in memory, and returns a human-readable response.

This project is intentionally small and modular, serving as a reference architecture for building simple AI agents with:
- Clear separation of concerns
- Explicit memory management
- Deterministic behavior
- HTTP-based interaction

## Features
- Memory-augmented agent loop
- OpenWeather API integration
- FastAPI HTTP service
- Bounded in-memory event store
- Modular, refactored codebase

## Requirements
- Python 3.9+
- OpenWeather API key

## Installation
```bash
pip install fastapi uvicorn requests pydantic
```

## Configuration
Set your OpenWeather API key as an environment variable:
```bash
export OPENWEATHER_API_KEY=your_api_key_here
```

## Running the Service
```bash
uvicorn src.agent_clima:app --reload
```

The API will be available at:
```
http://127.0.0.1:8000
```

## API Endpoints

### POST /climate
Fetches the current climate for a city.

**Request**
```json
{ "city": "São Paulo" }
```

**Response**
```json
{ "response": "Clima em São Paulo: 22°C, céu limpo" }
```

### GET /memory
Returns the most recent climate perceptions stored by the agent.

## Project Structure
```
architect/
├── README.md
└── src/
    ├── agent_clima.py      # FastAPI entrypoint
    └── architect/
        ├── agent.py        # Climate agent logic
        ├── memory.py       # Bounded in-memory store
        └── weather.py      # OpenWeather client
```

## License
MIT
