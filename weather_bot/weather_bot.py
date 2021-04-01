import speech_recognition as sr

from api import get_weather_data
from query import QueryOptions, query_weather_bot
from response import (
  ask_if_query_again,
  ask_name,
  greet,
  say_goodbye,
  say_hello,
)


def run_weather_bot():
  recognizer = sr.Recognizer()

  with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    call_dt, data = get_weather_data()
    query = True

    say_hello()
    name = ask_name(source, recognizer)
    greet(name)

    while query:
      query_weather_bot(call_dt, data, source, recognizer)
      query_again = ask_if_query_again(source, recognizer)

      if QueryOptions.do_not_query_again.value in query_again:
        query = False

    say_goodbye()


if __name__ == "__main__":
  run_weather_bot()
