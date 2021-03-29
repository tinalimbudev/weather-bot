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


def get_current_weather(data):
  current_data = data["current"]
  temp = current_data["temp"]
  feels_like = current_data["feels_like"]
  return temp, feels_like


def get_weather_after_some_hours(data, num_of_hours):
  # TODO
  return data


def get_weather_after_some_days(data, num_of_days):
  # TODO
  return data


# def report_current_weather():
#   data = get_weather_data()

#   weather = data["weather"]["main"]
#   temp = data["main"]["temp"]
#   feels_like = data["main"]["feels_like"]
#   temp_min = data["main"]["temp_min"]
#   temp_max = data["main"]["temp_max"]

#   respond_dynamically(
#     f"Today is looking {weather}. The current temperature is {temp} degrees "
#     f"celcius and feels like {feels_like}. The coldest today will be is "
#     f"{temp_min} degrees celcius, and the warmest today will be is {temp_max}."
#   )
