import os
import requests

API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in OPENWEATHER_API_KEY")

CITY = "Tomaszów Lubelski"
COUNTRY = "PL"

def get_current_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Error fetching weather: {data.get('message')}")
            return
        
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather in {CITY}: {weather_desc}")
        print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"Wind speed: {wind_speed} m/s")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_current_weather()