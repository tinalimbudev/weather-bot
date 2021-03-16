import os

from gtts import gTTS


def generate_audio_file_from_text(
  text, file_name, file_type="mp3", language="en", slow=False
):
  audio = gTTS(text=text, lang=language, slow=slow)
  audio.save(f"{file_name}.{file_type}")


if __name__ == "__main__":
  texts_and_file_names = [("Please could you repeat that?", "pardon")]

  for text, file_name in texts_and_file_names:
    generate_audio_file_from_text(text, file_name)
