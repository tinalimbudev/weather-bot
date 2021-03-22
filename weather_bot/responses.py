import os

from enum import Enum
from pathlib import Path
from playsound import playsound


class CommonAudioResponses(Enum):
  GREETING = "greeting"
  PARDON = "pardon"


COMMON_AUDIO_FILES = {
  CommonAudioResponses.GREETING: "greeting.mp3",
  CommonAudioResponses.PARDON: "pardon.mp3"
}


def get_common_audio_file_path(response_type):
  return os.path.join(
    Path().absolute(),
    "weather_bot",
    "media",
    "common_audio_responses",
    COMMON_AUDIO_FILES[response_type],
  )


def greet():
  audio_file_path = get_common_audio_file_path(CommonAudioResponses.GREETING)
  playsound(audio_file_path)


def beg_pardon():
  audio_file_path = get_common_audio_file_path(CommonAudioResponses.PARDON)
  playsound(audio_file_path)
