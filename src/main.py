import requests
import os
from save_to_db import save_data_to_db

API_URL = "https://dadosabertos.aneel.gov.br/api/3/action/datastore_search"
RESOURCE_ID = "ff80dd21-eade-4eb5-9ca8-d802c883940e"

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

if not OPENWEATHERMAP_API_KEY:
    raise ValueError("OPENWEATHERMAP_API_KEY is not set in the .env file.")

OPENWEATHERMAP_QUERY = os.getenv("OPENWEATHERMAP_QUERY")

if not OPENWEATHERMAP_QUERY:
    raise ValueError("OPENWEATHERMAP_QUERY is not set in the .env file.")

def fetch_aneel_data(limit=10):
    params = {"resource_id": RESOURCE_ID, "limit": limit}
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["result"]["records"]
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def fetch_weather_data():
    params = {"q": OPENWEATHERMAP_QUERY, "appid": OPENWEATHERMAP_API_KEY}
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch weather data: {response.status_code}")
        return []

if __name__ == "__main__":
    aneel_data = fetch_aneel_data(limit=10)
    
    if aneel_data:
        save_data_to_db(aneel_data)
    else:
        print("No energy data to save.")

    weather_data = fetch_weather_data()

    if weather_data:
        print("--- Weather Data ---")
        print(f"Coordinates: {weather_data['coord']['lon']}, {weather_data['coord']['lat']}")
        print(f"Country: {weather_data['sys']['country']}")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']} Kelvin")
        print(f"Feels like: {weather_data['main']['feels_like']} Kelvin")
        print(f"Minimum temperature: {weather_data['main']['temp_min']} Kelvin")
        print(f"Maximum temperature: {weather_data['main']['temp_max']} Kelvin")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Pressure: {weather_data['main']['pressure']} hPa")
        print(f"Visibility: {weather_data['visibility']} meters")
        print(f"Wind speed: {weather_data['wind']['speed']} m/s")
        print(f"Wind direction: {weather_data['wind']['deg']} degrees")
        print(f"Cloudiness: {weather_data['clouds']['all']}%")
        print(f"Sunrise: {weather_data['sys']['sunrise']}")
        print(f"Sunset: {weather_data['sys']['sunset']}")
    else:
        print("No weather data to display.")
