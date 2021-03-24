from datetime import datetime
import os

from gtts import gTTS
from pathlib import Path
from playsound import playsound

from generate_audio_file import generate_audio_file_from_text


def respond_dynamically(text):
  # TODO: Make this work using tempfile instead.

  file_name = f"temp_audio_file_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
  file_path = generate_audio_file_from_text(text, file_name, common=False)
  playsound(file_path)
  os.remove(file_path)
