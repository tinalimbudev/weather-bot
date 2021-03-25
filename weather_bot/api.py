import requests

from decouple import config


WEATHER_API_KEY = config("WEATHER_API_KEY")


def get_weather_for_today():
  response = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?appid={WEATHER_API_KEY}&"
    f"q=London"
  )
  return response.json()
