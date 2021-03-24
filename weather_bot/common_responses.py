import os

from enum import Enum
from functools import partial
from pathlib import Path
from playsound import playsound


class CommonResponseTypes(Enum):
  GREETING = "greeting"
  PARDON = "pardon"


COMMON_RESPONSES = {
  CommonResponseTypes.GREETING: "greeting.mp3",
  CommonResponseTypes.PARDON: "pardon.mp3"
}


def play_common_response(response_type):
  audio_file_path = os.path.join(
    Path().absolute(),
    "weather_bot",
    "media",
    "common_responses",
    COMMON_RESPONSES[response_type],
  )
  playsound(audio_file_path)


greet = partial(
  play_common_response, response_type=CommonResponseTypes.GREETING
)
beg_pardon = partial(
  play_common_response, response_type=CommonResponseTypes.PARDON
)
