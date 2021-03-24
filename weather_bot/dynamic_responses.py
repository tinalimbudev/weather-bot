import os

from gtts import gTTS
from pathlib import Path
from playsound import playsound

from generate_audio_file import generate_audio_file_from_text


def respond_dynamically(text):
  # TODO: Make this work using tempfile instead.
  # TODO: Add a timestamp.
  audio_file_path = generate_audio_file_from_text(
    text, "temp_audio_file", common=False
  )
  playsound(audio_file_path)
  os.remove(audio_file_path)
