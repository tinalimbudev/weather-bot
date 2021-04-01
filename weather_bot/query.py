from enum import Enum

from api import (
  extract_weather_data_for_later_day,
  extract_weather_data_for_later_time,
  get_weather_data,
)


class QueryOptions(Enum):
  today = "today"
  different_day = "different day"
  now = "now"
  later = "later"
  query_again = "yes"
  do_not_query_again = "no"


def query_weather_bot(source, recognizer):
  from response import (
    ask_how_many_days,
    ask_how_many_hours,
    ask_if_now_or_later,
    ask_if_today_or_different_day,
  )

  # TODO: In addition to just temperature, report additional weather data.

  call_dt, data = get_weather_data()
  today_or_not = ask_if_today_or_different_day(source, recognizer)

  if QueryOptions.today.value in today_or_not:
    now_or_later = ask_if_now_or_later(source, recognizer)

    if QueryOptions.now.value in now_or_later:
      query_current_weather(data)

    elif QueryOptions.later.value in now_or_later:
      num_of_hours = ask_how_many_hours(source, recognizer)
      query_weather_for_later_time(call_dt, data, int(num_of_hours))

  elif QueryOptions.different_day.value in today_or_not:
    num_of_days = ask_how_many_days(source, recognizer)
    query_weather_for_later_day(call_dt, data, int(num_of_days))


def query_current_weather(data):
  from response import report_current_weather

  report_current_weather(data["current"]["temp"])


def query_weather_for_later_time(call_dt, data, num_of_hours):
  from response import missing_data, report_weather_for_later_time

  data = extract_weather_data_for_later_time(call_dt, data, num_of_hours)

  if data is None:
    missing_data()
  else:
    report_weather_for_later_time(data["temp"])


def query_weather_for_later_day(call_dt, data, num_of_days):
  from response import missing_data, report_weather_for_later_day

  data = extract_weather_data_for_later_day(call_dt, data, num_of_days)

  if data is None:
    missing_data()
  else:
    temp = data["temp"]
    report_weather_for_later_day(temp["day"], temp["eve"])
