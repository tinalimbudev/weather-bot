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
  Cities.porto: (41.157944, -8.629105),
}


def get_weather_data(lang="en", units="metric", city=Cities.london):
  call_dt = datetime.now().replace(minute=0, second=0, microsecond=0)

  try:
    lat, lon = CITY_TO_LAT_AND_LON[city]
  except KeyError:
    raise NotImplementedError

  api_key = config("WEATHER_API_KEY")
  api_url = (
    f"https://api.openweathermap.org/data/2.5/onecall?appid={api_key}"
    f"&lang={lang}&units={units}&lat={lat}&lon={lon}&exclude=minutely,alerts"
  )
  data = requests.get(api_url).json()

  return call_dt, data
