import os

from gtts import gTTS
from pathlib import Path


def generate_audio_file_from_text(
  text, file_name, file_type="mp3", language="en", slow=False
):
  audio = gTTS(text=text, lang=language, slow=slow)
  file_path = os.path.join(
    Path().absolute(),
    "media",
    "common_responses",
    f"{file_name}.{file_type}",
  )
  audio.save(file_path)
  return file_path


if __name__ == "__main__":
  # Replace with list of tuples.
  # E.g. [("Please could you repeat that?", "pardon")]
  texts_and_file_names = []

  for text, file_name in texts_and_file_names:
    generate_audio_file_from_text(text, file_name)
