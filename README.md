# Architect Climate Agent

This repository contains a simple **memory-augmented climate agent** implemented in Python using FastAPI.

## Overview

The agent exposes an HTTP API that:

- Fetches real-time weather data from OpenWeather
- Generates a human-readable climate response
- Stores all perceptions in an in-memory log (agent memory)

The project is intentionally minimal and designed as a reference architecture for building agent-style services.

## Architecture

- `ClimateAgent`: Core agent loop (perceive → decide → act)
- `OpenWeatherClient`: External weather API integration
- `Memory`: Lightweight in-memory storage for agent perceptions
- `FastAPI app`: HTTP interface for interacting with the agent

## API Endpoints

### `POST /climate`

Request weather information for a city.

```json
{
  "city": "Berlin"
}
```

Response:

```json
{
  "response": "Clima em Berlin: 18°C, clear sky"
}
```

### `GET /memory`

Returns the internal agent memory containing all previous perceptions.

## Configuration

Set the OpenWeather API key as an environment variable:

```bash
export OPENWEATHER_API_KEY=your_api_key_here
```

## Running the Server

```bash
uvicorn agent_clima:app --reload
```

## Purpose

This project demonstrates how to structure a simple AI/agent-style service with clear separation of concerns, deterministic behavior, and extensibility for more advanced reasoning or long-term memory backends.
