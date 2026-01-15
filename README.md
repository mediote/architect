# Architect – Climate Agent

This repository contains a refactored **Climate Agent** implemented in Python using **FastAPI** and a simple **Memory-Augmented Framework (MAF)**.

## Features

- Fetches real-time weather data from OpenWeather
- Memory-bounded event storage
- Clean agent lifecycle: perceive → decide → act
- FastAPI HTTP interface

## Requirements

- Python 3.10+
- OpenWeather API key

## Setup

```bash
pip install fastapi uvicorn requests pydantic
export OPENWEATHER_API_KEY=your_api_key_here
```

## Running the API

```bash
uvicorn src.agent_clima:app --reload
```

## API Endpoints

### `POST /climate`

Request body:
```json
{ "city": "Sao Paulo" }
```

Response:
```json
{ "response": "Clima em Sao Paulo: 25°C, céu limpo" }
```

### `GET /memory`

Returns the in-memory history of weather queries.

## Architecture

- `ClimateAgent`: core agent logic
- `OpenWeatherClient`: external API adapter
- `Memory`: bounded in-memory event store
- FastAPI app factory for clean initialization

## License

MIT
