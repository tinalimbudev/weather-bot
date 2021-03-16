import os

from gtts import gTTS


def generate_audio_file_from_text(
  text, output_folder_path, file_name, file_type="mp3", language="en", slow=False
):
  audio = gTTS(text=text, lang=language, slow=slow)
  file_path = f"{output_folder_path}/{file_name}.{file_type}"
  audio.save(file_path)


if __name__ == "__main__":
  texts_and_file_names = [("Please could you repeat that?", "pardon")]

  for text, file_name in texts_and_file_names:
    generate_audio_file_from_text(text, "media/common_audio_responses", file_name)
