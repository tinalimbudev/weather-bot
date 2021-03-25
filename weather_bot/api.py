import requests

from decouple import config


def get_weather_for_today():
  # TODO: Make this more flexible.
  api_key = config("WEATHER_API_KEY")
  response = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q=London"
  )
  return response.json()
