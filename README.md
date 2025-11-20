# Weather-Information-api
A FastAPI-based Weather API that fetches real-time weather data using the OpenWeather service.
# Weather API (FastAPI)

A simple FastAPI project that fetches real-time weather data using the OpenWeather API.

## Features
- GET /weather/{city}
- Real-time temperature, humidity, description, wind speed
- Clean API response model (Pydantic)
- Tested with Uvicorn

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Create .env file:
   API_KEY=your_api_key_here

3. Run server:
   uvicorn main:app --reload

