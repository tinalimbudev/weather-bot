import requests

from datetime import datetime, timedelta
from decouple import config
from enum import Enum


class Cities(Enum):
  kathmandu = "Kathmandu"
  london = "London"
  porto = "Porto"


LONDON_LAT = 51.507351
LONDON_LON = -0.127758
CITY_TO_LAT_AND_LON = {
  Cities.kathmandu: (27.717245, 85.323959),
  Cities.london: (LONDON_LAT, LONDON_LON),
}


def get_weather_data(lang="en", units="metric", city=Cities.london):
  call_dt = datetime.now().replace(minute=0, second=0, microsecond=0)

  api_key = config("WEATHER_API_KEY")
  lat, lon = CITY_TO_LAT_AND_LON.get(city, (LONDON_LAT, LONDON_LON))
  api_url = (
    f"https://api.openweathermap.org/data/2.5/onecall?appid={api_key}"
    f"&lang={lang}&units={units}&lat={lat}&lon={lon}&exclude=minutely,alerts"
  )
  data = requests.get(api_url).json()

  return call_dt, data


def get_weather_data_for_later_time(call_dt, hourly_data, num_of_hours):
  if num_of_hours <= 12:
    hourly_data = {d["dt"]: d for d in hourly_data}
    requested_dt = call_dt + timedelta(hours=num_of_hours)
    requested_timestamp = int(requested_dt.timestamp())

    try:
      return hourly_data[requested_timestamp]
    except KeyError:
      return None


def get_weather_data_for_later_day(call_dt, daily_data, num_of_days):
  if num_of_days <= 7:
    daily_data = {
      datetime.fromtimestamp(d["dt"]).replace(hour=0, minute=0): d for d in daily_data
    }
    requested_dt = call_dt.replace(hour=0) + timedelta(days=num_of_days)

    try:
      return daily_data[requested_dt]
    except KeyError:
      return None


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
