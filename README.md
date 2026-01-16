# Architect Climate Agent

This repository contains a simple **memory-augmented climate agent** implemented in Python. The agent retrieves real-time weather data from the OpenWeather API, stores recent interactions in memory, and exposes a small HTTP API using **FastAPI**.

## Features

- Fetches current weather data by city name
- Generates human-readable climate responses (Portuguese)
- Stores recent queries in a bounded in-memory store
- Exposes REST endpoints via FastAPI

## Project Structure

```
src/
  agent_clima.py        # FastAPI application entrypoint
  architect/
    __init__.py         # Package exports
    agent.py            # ClimateAgent implementation
    memory.py           # Simple bounded memory
    weather.py          # OpenWeather API client
```

## Requirements

- Python 3.9+
- An OpenWeather API key

## Installation

```bash
pip install fastapi uvicorn requests
```

## Configuration

Set your OpenWeather API key as an environment variable:

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

## Running the API

```bash
uvicorn src.agent_clima:app --reload
```

## API Endpoints

### `POST /climate`

Request body:

```json
{ "city": "São Paulo" }
```

Response:

```json
{ "response": "Clima em São Paulo: 25°C, céu limpo" }
```

### `GET /memory`

Returns the list of recent climate queries stored in memory.

## License

MIT
