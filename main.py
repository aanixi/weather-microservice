from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "64da33cbf300091cb266d5350a596166"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather")
def get_weather(city: str):

    try:
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})

        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        else:
            return {
                "error": "City not found",
                "status code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": "Server error", "details": str(e)}
