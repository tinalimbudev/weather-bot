from enum import Enum

from api import (
  extract_weather_data_for_later_day,
  extract_weather_data_for_later_time,
  get_weather_data,
)
from response import (
  ask_how_many_days,
  ask_how_many_hours,
  ask_if_current_time_or_different,
  ask_if_today_or_different_day,
  report_current_weather,
  report_weather_for_later_day,
  report_weather_for_later_time,
)


class QueryOptions(Enum):
  today = "today"
  different_day = "different day"
  current_time = "current"
  different_time = "different time"
  query_again = "yes"
  do_not_query_again = "no"


def query_weather_bot(call_dt, data, source, recognizer):
  call_dt, data = get_weather_data()
  today_or_not = ask_if_today_or_different_day(source, recognizer)

  if QueryOptions.today.value in today_or_not:
    current_time_or_not = ask_if_current_time_or_different(source, recognizer)

    if QueryOptions.current_time.value in current_time_or_not:
      query_current_weather(data)

    elif QueryOptions.different_time.value in current_time_or_not:
      num_of_hours = ask_how_many_hours(source, recognizer)
      query_weather_for_later_time(call_dt, data, int(num_of_hours))

  elif QueryOptions.different_day.value in today_or_not:
    num_of_days = ask_how_many_days(source, recognizer)
    query_weather_for_later_day(call_dt, data, int(num_of_days))


def query_current_weather(data):
  report_current_weather(data["current"]["temp"])


def query_weather_for_later_time(call_dt, data, num_of_hours):
  data = extract_weather_data_for_later_time(call_dt, data, num_of_hours)
  report_weather_for_later_time(data["temp"])


def query_weather_for_later_day(call_dt, data, num_of_days):
  temp = extract_weather_data_for_later_day(call_dt, data, num_of_days)["temp"]
  report_weather_for_later_day(temp["day"], temp["eve"])
