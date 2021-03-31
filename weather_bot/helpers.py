from datetime import datetime
import os

from enum import Enum
from functools import partial
from gtts import gTTS
from pathlib import Path
from playsound import playsound
import speech_recognition as sr

from generate_audio_file import generate_audio_file_from_text


class QueryOptions(Enum):
  today = "today"
  different_day = "different_day"
  current_time = "current"
  different_time = "different time"
  query_again = "yes"
  do_not_query_again = "no"


class ResponseTypes(Enum):
  ask_current_or_not = "ask_current_or_not"
  ask_how_many_days = "ask_how_many_days"
  ask_how_many_hours = "ask_how_many_hours"
  ask_if_query_again = "ask_if_query_again"
  ask_name = "ask_name"
  ask_today_or_not = "ask_today_or_not"
  goodbye = "goodbye"
  hello = "hello"
  invalid_input = "invalid_input"
  pardon = "pardon"


RESPONSE_FILES = {
  ResponseTypes.ask_current_or_not: "ask_current_or_not.mp3",
  ResponseTypes.ask_how_many_days: "ask_how_many_days.mp3",
  ResponseTypes.ask_how_many_hours: "ask_how_many_hours.mp3",
  ResponseTypes.ask_if_query_again: "ask_if_query_again.mp3",
  ResponseTypes.ask_name: "ask_name.mp3",
  ResponseTypes.ask_today_or_not: "ask_today_or_not.mp3",
  ResponseTypes.goodbye: "goodbye.mp3",
  ResponseTypes.hello: "hello.mp3",
  ResponseTypes.invalid_input: "invalid_input.mp3",
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
goodbye = partial(play_common_response, response_type=ResponseTypes.goodbye)
hello = partial(play_common_response, response_type=ResponseTypes.hello)
invalid_input = partial(
  play_common_response, response_type=ResponseTypes.invalid_input
)


def listen_and_transcribe(audio_source, recognizer):
  audio = recognizer.listen(audio_source)

  try:
    return recognizer.recognize_google(audio)
  except sr.UnknownValueError:
    beg_pardon()
    return listen_and_transcribe(audio_source, recognizer)


def play_common_response_and_get_input(response_type, audio_source, recognizer):
  play_common_response(response_type)
  return listen_and_transcribe(audio_source, recognizer)


def get_expected_input(expected_inputs, audio_source, recognizer):
  input = listen_and_transcribe(audio_source, recognizer)

  if not any([i in input for i in expected_inputs]):
    invalid_input()
    return get_expected_input(expected_inputs, audio_source, recognizer)


def play_common_response_and_get_expected_input(
  response_type, expected_inputs, audio_source, recognizer
):
  play_common_response(response_type)
  return get_expected_input(expected_inputs, audio_source, recognizer)


def ask_name(audio_source, recognizer):
  return play_common_response_and_get_input(
    ResponseTypes.ask_name, audio_source, recognizer
  )


def ask_today_or_not(expected_responses, audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_today_or_not,
    [QueryOptions.today, QueryOptions.different_day],
    audio_source,
    recognizer,
  )


def ask_current_or_not(expected_responses, audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_current_or_not,
    [QueryOptions.current_time, QueryOptions.different_time],
    audio_source,
    recognizer,
  )


def ask_how_many_hours(expected_responses, audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_how_many_hours,
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    audio_source,
    recognizer,
  )


def ask_how_many_days(expected_responses, audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_how_many_days,
    [1, 2, 3, 4, 5, 6, 7],
    audio_source,
    recognizer,
  )


def ask_if_query_again(expected_responses, audio_source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_if_query_again,
    [QueryOptions.query_again, QueryOptions.do_not_query_again],
    audio_source,
    recognizer,
  )


def respond_dynamically(text):
  # TODO: Make this work using tempfile instead.

  file_name = f"temp_audio_file_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
  file_path = generate_audio_file_from_text(text, file_name, common=False)
  playsound(file_path)
  os.remove(file_path)


def greet(name):
  respond_dynamically(f"Nice to meet you {name}!")


def report_current_weather(temp, feels_like):
  respond_dynamically(
    f"The current temperature is {temp} degrees celcius and feels like "
    f"{feels_like} degrees celcius."
  )


def report_weather_for_later_time(temp, feels_like):
  respond_dynamically(
    f"The temperature at the time that you requested will be {temp} degrees "
    f"celcius and it will feel like {feels_like} degrees celcius."
  )


def report_weather_for_later_day(temp, feels_like):
  respond_dynamically(
    f"The temperature at the day that you requested will be {temp} degrees "
    f"celcius and it will feel like {feels_like} degrees celcius."
  )
