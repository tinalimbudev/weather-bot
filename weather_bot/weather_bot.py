import speech_recognition as sr

from api import get_full_weather_data, extract_weather_data, get_weather_data_for_later_time, get_weather_data_for_later_day
from helpers import hello, ask_name, greet, ask_today_or_not, report_current_weather, ask_current_or_not, ask_how_many_hours, ask_how_many_days, report_weather_for_later_time, report_weather_for_later_day, ask_if_query_again, goodbye


TODAY = "today"
DIFFERENT_DAY = "different_day"
CURRENT = "current"
DIFFERENT_TIME = "different time"
YES = "yes"
NO = "no"


def run_weather_bot():
  recognizer = sr.Recognizer()

  with sr.Microphone() as audio_source:
    recognizer.adjust_for_ambient_noise(audio_source, duration=0.5)
    call_dt, data = get_full_weather_data()
    query = True

    hello()
    name = ask_name(audio_source, recognizer)
    greet(name)

    while query:
      query_weather_bot(call_dt, data, audio_source, recognizer)
      query_again = ask_if_query_again([YES, NO], audio_source, recognizer)

      if NO in query_again:
        query = False

    goodbye()


def query_weather_bot(call_dt, data, audio_source, recognizer):
  today_or_not = ask_today_or_not(
    [TODAY, DIFFERENT_DAY], audio_source, recognizer
  )

  if TODAY in today_or_not:
    current_or_not = ask_current_or_not(
      [CURRENT, DIFFERENT_TIME] audio_source, recognizer
    )

    if CURRENT in current_or_not:
      query_current_weather(data)

    elif DIFFERENT_TIME in current_or_not:
      num_of_hours = ask_how_many_hours(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        audio_source,
        recognizer,
      )
      query_weather_for_later_time(data, num_of_hours)

  elif DIFFERENT_DAY in today_or_not:
    num_of_days = ask_how_many_days(
      [1, 2, 3, 4, 5, 6, 7], audio_source, recognizer
    )
    query_weather_for_later_day(data, num_of_days)


def query_current_weather(data):
  temp, feels_like = extract_weather_data(data["current"])
  report_current_weather(temp, feels_like)


def query_weather_for_later_time(data, num_of_hours):
  data = get_weather_data_for_later_time(
    call_dt, data["hourly_data"], num_of_hours
  )
  temp, feels_like = extract_weather_data(data)
  report_weather_for_later_time(temp, feels_like)


def query_weather_for_later_day(data, num_of_days):
  data = get_weather_data_for_later_day(
    call_dt, data["daily_data"], num_of_days
  )
  temp, feels_like = extract_weather_data(data)
  report_weather_for_later_day(temp, feels_like)


if __name__ == "__main__":
  run_weather_bot()
