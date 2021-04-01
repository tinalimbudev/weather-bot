from datetime import datetime
import os

from enum import Enum
from functools import partial
from pathlib import Path
from playsound import playsound
import speech_recognition as sr

from generate_audio_files import generate_audio_file_from_text


class ResponseTypes(Enum):
  ask_how_many_days = "ask_how_many_days"
  ask_how_many_hours = "ask_how_many_hours"
  ask_if_now_or_later = "ask_if_now_or_later"
  ask_if_query_again = "ask_if_query_again"
  ask_if_today = "ask_if_today"
  ask_name = "ask_name"
  goodbye = "goodbye"
  hello = "hello"
  invalid_input = "invalid_input"
  missing_data = "missing_data"
  pardon = "pardon"


RESPONSE_FILES = {
  ResponseTypes.ask_how_many_days: "ask_how_many_days.mp3",
  ResponseTypes.ask_how_many_hours: "ask_how_many_hours.mp3",
  ResponseTypes.ask_if_now_or_later: "ask_if_now_or_later.mp3",
  ResponseTypes.ask_if_query_again: "ask_if_query_again.mp3",
  ResponseTypes.ask_if_today: "ask_if_today.mp3",
  ResponseTypes.ask_name: "ask_name.mp3",
  ResponseTypes.goodbye: "goodbye.mp3",
  ResponseTypes.hello: "hello.mp3",
  ResponseTypes.invalid_input: "invalid_input.mp3",
  ResponseTypes.missing_data: "missing_data.mp3",
  ResponseTypes.pardon: "pardon.mp3",
}


def play_common_response(response_type):
  file_path = os.path.join(
    Path().absolute(),
    "weather_bot",
    "media",
    "common_responses",
    RESPONSE_FILES[response_type],
  )
  playsound(file_path)


beg_pardon = partial(play_common_response, response_type=ResponseTypes.pardon)
flag_invalid_input = partial(
  play_common_response, response_type=ResponseTypes.invalid_input
)
missing_data = partial(
  play_common_response, response_type=ResponseTypes.missing_data
)
say_goodbye = partial(play_common_response, response_type=ResponseTypes.goodbye)
say_hello = partial(play_common_response, response_type=ResponseTypes.hello)


def get_input(source, recognizer):
  audio = recognizer.listen(source)

  try:
    return recognizer.recognize_google(audio)
  except sr.UnknownValueError:
    beg_pardon()
    return get_input(source, recognizer)


def play_common_response_and_get_input(response_type, source, recognizer):
  play_common_response(response_type)
  return get_input(source, recognizer)


def ask_name(source, recognizer):
  return play_common_response_and_get_input(
    ResponseTypes.ask_name, source, recognizer
  )


def get_expected_input(expected_inputs, source, recognizer):
  input = get_input(source, recognizer)

  if not any([i in input for i in expected_inputs]):
    flag_invalid_input()
    return get_expected_input(expected_inputs, source, recognizer)
  else:
    return input


def play_common_response_and_get_expected_input(
  response_type, expected_inputs, source, recognizer
):
  play_common_response(response_type)
  return get_expected_input(expected_inputs, source, recognizer)


def ask_if_today_or_different_day(source, recognizer):
  from query import QueryOptions

  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_if_today,
    [QueryOptions.today.value, QueryOptions.different_day.value],
    source,
    recognizer,
  )


def ask_if_now_or_later(source, recognizer):
  from query import QueryOptions

  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_if_now_or_later,
    [QueryOptions.now.value, QueryOptions.later.value],
    source,
    recognizer,
  )


def ask_how_many_hours(source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_how_many_hours,
    [str(i) for i in range(1, 13)],
    source,
    recognizer,
  )


def ask_how_many_days(source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_how_many_days,
    [str(i) for i in range(1, 8)],
    source,
    recognizer,
  )


def ask_if_query_again(source, recognizer):
  from query import QueryOptions

  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_if_query_again,
    [QueryOptions.query_again.value, QueryOptions.do_not_query_again.value],
    source,
    recognizer,
  )


def respond_dynamically(text):
  # TODO: Make this work using tempfile instead.

  file_name = f"temp_audio_file_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
  file_path = generate_audio_file_from_text(text, file_name)
  playsound(file_path)
  os.remove(file_path)


def greet(name):
  respond_dynamically(f"Nice to meet you {name}!")


def report_current_weather(temp):
  respond_dynamically(
    f"The current temperature is {temp} degrees celcius."
  )


def report_weather_for_later_time(temp):
  respond_dynamically(
    f"The temperature at the time that you requested for will be {temp} "
    "degrees celcius."
  )


def report_weather_for_later_day(temp_day, temp_eve):
  respond_dynamically(
    f"The temperature on the day that you requested for will be {temp_day} "
    f"degrees celcius in the day time, and {temp_eve} degrees celcius in the "
    f"evening."
  )
