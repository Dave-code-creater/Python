from dotenv import load_dotenv
import os
import requests

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API")
print(WEATHER_API_KEY)

def check_API():
    if WEATHER_API_KEY is None:
        raise Exception("API key not found.")
    else:
        print("API key found.")

def get_weather(city="Toronto",country="Canada"):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "q": city,
        "country": country,
        "key": WEATHER_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)

def main():
    check_API()
    get_weather()

if __name__ == "__main__":
    main()