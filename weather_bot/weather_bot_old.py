import speech_recognition as sr

from api import get_full_weather_data, extract_weather_data, get_weather_data_for_later_time, get_weather_data_for_later_day
from helpers import hello, ask_name, greet, ask_today_or_not, report_current_weather, ask_current_or_not, ask_how_many_hours, ask_how_many_days, report_weather_for_later_time, report_weather_for_later_day, ask_if_query_again, goodbye, QueryOptions


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
      query_again = ask_if_query_again(audio_source, recognizer)

      if QueryOptions.do_not_query_again.value in query_again:
        query = False

    goodbye()


if __name__ == "__main__":
  run_weather_bot()
