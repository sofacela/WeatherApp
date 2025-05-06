import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

AUTHOR = "Sofiia Laba" 
PORT = int(os.environ.get("APP_PORT", 8000))

@app.on_event("startup")
async def startup_event():
    print(f"Startup Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Author: {AUTHOR}")
    print(f"Port: {PORT}")

LOCATIONS = {
    "Poland": ["Warsaw", "Krakow", "Gdansk"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "Spain": ["Madrid", "Barcelona", "Valencia"]
}

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("static/index.html", "r") as f:
        return f.read()

@app.get("/weather/{country}/{city}")
async def get_weather(country: str, city: str):
    if country not in LOCATIONS or city not in LOCATIONS[country]:
        raise HTTPException(status_code=404, detail="Invalid country or city")

    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Weather API key not provided")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")

    data = response.json()
    return {
        "city": city,
        "country": country,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)