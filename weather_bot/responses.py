import os

from enum import Enum
from functools import partial
from gtts import gTTS
from pathlib import Path
from playsound import playsound


class CommonAudioResponses(Enum):
  GREETING = "greeting"
  PARDON = "pardon"


COMMON_AUDIO_FILES = {
  CommonAudioResponses.GREETING: "greeting.mp3",
  CommonAudioResponses.PARDON: "pardon.mp3"
}


def play_common_audio_response(response_type):
  audio_file_path = os.path.join(
    Path().absolute(),
    "weather_bot",
    "media",
    "common_audio_responses",
    COMMON_AUDIO_FILES[response_type],
  )
  playsound(audio_file_path)


greet = partial(play_common_audio_response, response_type=CommonAudioResponses.GREETING)
beg_pardon = partial(play_common_audio_response, response_type=CommonAudioResponses.PARDON)


# def respond_dynamically(text):
#   # TODO: Make this work using tempfile instead.

#   audio = gTTS(text=text, lang="en", slow=False)  # TODO: Consolidate.
#   audio_file_path = os.path.join(
#     Path().absolute(),
#     "weather_bot",
#     "media",
#     "audio_responses",
#     "temp_audio_file.mp3",
#   )
#   # TODO: Add timestamp.
#   audio.save(audio_file_path)
#   playsound(audio_file_path)
#   os.remove(audio_file_path)
