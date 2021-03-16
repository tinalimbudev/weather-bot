from gtts import gTTS


OUTPUT_FOLDER_PATH = ""  # Replace with output folder path.
TEXTS_AND_FILE_NAME = []  # Replace with list of tuples.


def generate_audio_file_from_text(
  text, output_folder_path, file_name, file_type="mp3", language="en", slow=False
):
  audio = gTTS(text=text, lang=language, slow=slow)
  file_path = f"{output_folder_path}/{file_name}.{file_type}"  # TODO: safe join
  audio.save(file_path)
  return file_path


if __name__ == "__main__":
  for text, file_name in TEXTS_AND_FILE_NAME:
    generate_audio_file_from_text(text, file_name, OUTPUT_FOLDER_PATH)
