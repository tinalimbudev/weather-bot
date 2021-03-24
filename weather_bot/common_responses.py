import os

from enum import Enum
from functools import partial
from pathlib import Path
from playsound import playsound


class CommonResponseTypes(Enum):
  HELLO = "hello"
  ASK_NAME = "ask_name"
  PARDON = "pardon"
  TODAY_OR_NOT = "today_or_not"


COMMON_RESPONSES = {
  CommonResponseTypes.HELLO: "hello.mp3",
  CommonResponseTypes.ASK_NAME: "ask_name.mp3",
  CommonResponseTypes.PARDON: "pardon.mp3",
  CommonResponseTypes.TODAY_OR_NOT: "today_or_not.mp3",
}


def play_common_response(response_type):
  file_path = os.path.join(
    Path().absolute(),
    "weather_bot",
    "media",
    "common_responses",
    COMMON_RESPONSES[response_type],
  )
  playsound(file_path)


hello = partial(
  play_common_response, response_type=CommonResponseTypes.HELLO
)
as_name = partial(
  play_common_response, response_type=CommonResponseTypes.ASK_NAME
)
beg_pardon = partial(
  play_common_response, response_type=CommonResponseTypes.PARDON
)
today_or_not = partial(
  play_common_response, response_type=CommonResponseTypes.TODAY_OR_NOT
)
