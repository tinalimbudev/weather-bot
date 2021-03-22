import os

from gtts import gTTS
from pathlib import Path

from weather_bot import AUDIO_FILE_EXT, LANGUAGE


def generate_audio_file_from_text(
  text, file_name, file_type=AUDIO_FILE_EXT, language=LANGUAGE, slow=False
):
  audio = gTTS(text=text, lang=language, slow=slow)
  audio_file_path = os.path.join(
    Path().absolute(),
    f"weather_bot/media/common_audio_responses/{file_name}.{file_type}",
  )
  audio.save(audio_file_path)


if __name__ == "__main__":
  texts_and_file_names = [("Please could you repeat that?", "pardon")]

  for text, file_name in texts_and_file_names:
    generate_audio_file_from_text(text, file_name)
