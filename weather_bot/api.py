import requests

from decouple import config


WEATHER_API_KEY = config("WEATHER_API_KEY")

LONDON = "London"
LONDON_LAT = 51.507351
LONDON_LON = -0.127758

CITY_TO_LAT_AND_LON = {
  LONDON: (LONDON_LAT, LONDON_LON),
}


def get_weather_data(lang="en", units="metric", city=LONDON):
  lat, lon = CITY_TO_LAT_AND_LON_MAP.get(city, (LONDON_LAT, LONDON_LON))
  api_url = (
    f"https://api.openweathermap.org/data/2.5/onecall?appid={WEATHER_API_KEY}"
    f"&lang={lang}&units={units}&lat={lat}&lon={lon}&exclude=minutely,alerts"
  )
  return requests.get(api_url).json()
