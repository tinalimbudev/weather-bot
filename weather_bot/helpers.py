from datetime import datetime
import os

from enum import Enum
from functools import partial
from gtts import gTTS
from pathlib import Path
from playsound import playsound
import speech_recognition as sr

from generate_audio_file import generate_audio_file_from_text


class ResponseTypes(Enum):
  HELLO = "hello"
  ASK_NAME = "ask_name"
  PARDON = "pardon"
  ASK_TODAY_OR_NOT = "ask_today_or_not"


RESPONSE_FILES = {
  ResponseTypes.HELLO: "hello.mp3",
  ResponseTypes.ASK_NAME: "ask_name.mp3",
  ResponseTypes.PARDON: "pardon.mp3",
  ResponseTypes.ASK_TODAY_OR_NOT: "ask_today_or_not.mp3",
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


hello = partial(play_common_response, response_type=ResponseTypes.HELLO)
beg_pardon = partial(play_common_response, response_type=ResponseTypes.PARDON)


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


def ask_name(audio_source, recognizer):
  return play_common_response_and_get_input(
    ResponseTypes.ASK_NAME, audio_source, recognizer
  )


def ask_today_or_not(audio_source, recognizer):
  return play_common_response_and_get_input(
    ResponseTypes.ASK_TODAY_OR_NOT, audio_source, recognizer
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
