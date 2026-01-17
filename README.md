# Architect Climate Agent

A minimal, modular climate agent built with FastAPI that retrieves weather data from OpenWeather and produces human‑readable responses.

## Architecture

The project is organized around a small set of focused components:

- **ClimateAgent**: Orchestrates the workflow of fetching weather data, storing memory, and generating responses.
- **OpenWeatherClient**: Handles communication with the OpenWeather API.
- **ClimateResponseFormatter**: Converts raw API data into user‑facing text.
- **Memory**: Simple in‑memory storage of past interactions.

This separation of concerns makes the agent easy to test, extend, and maintain.

## Project Structure

```
src/
  app/            # FastAPI application
  architect/      # Core agent, memory, formatter, and weather client
  config/         # Configuration and settings
```

## Setup

1. Create a virtual environment and install dependencies.
2. Set the `OPENWEATHER_API_KEY` environment variable.
3. Run the FastAPI app.

Example:

```bash
export OPENWEATHER_API_KEY=your_api_key
uvicorn src.app.main:app --reload
```

## API Usage

### Get Climate Information

`POST /climate`

Request body:

```json
{ "city": "Lisbon" }
```

Response:

```json
{ "response": "Clima em Lisbon: 20°C, céu limpo" }
```

### View Agent Memory

`GET /memory`

Returns the list of stored interactions.

## Extensibility

- Swap out the weather client to support another provider.
- Replace the formatter for different languages or output formats.
- Persist memory to a database instead of in‑memory storage.

## License

MIT
