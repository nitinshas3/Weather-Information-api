from fastapi import FastAPI, HTTPException
from schema import WeatherResponse
from weather_service import weatherinfo

app = FastAPI(title="Weather Information API")

@app.get("/")
def home():
    return {"weather": "information"}

@app.get("/weather/{city}", response_model=WeatherResponse)
def weather(city: str):
    data = weatherinfo(city)

    if not data:
        raise HTTPException(status_code=404, detail="City not found")

    return data
