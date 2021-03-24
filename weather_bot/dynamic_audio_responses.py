import os

from gtts import gTTS
from pathlib import Path
from playsound import playsound


def respond_dynamically(text):
  # TODO: Make this work using tempfile instead.

  audio = gTTS(text=text, lang="en", slow=False)  # TODO: Consolidate.
  audio_file_path = os.path.join(
    Path().absolute(),
    "weather_bot",
    "media",
    "audio_responses",
    "temp_audio_file.mp3",
  )
  # TODO: Add timestamp.
  audio.save(audio_file_path)
  playsound(audio_file_path)
  os.remove(audio_file_path)
