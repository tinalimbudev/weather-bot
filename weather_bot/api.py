import requests

from decouple import config


WEATHER_API_KEY = config("WEATHER_API_KEY")


def get_current_weather(city_name="London", units="metric"):
  api_url = (
    f"http://api.openweathermap.org/data/2.5/weather?appid={WEATHER_API_KEY}"
    f"&q={city_name}&units={units}"
  )
  return requests.get(api_url).json()
