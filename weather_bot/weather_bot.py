import os
import speech_recognition as sr

from gtts import gTTS

from responses import greet


def run_weather_bot():
  recognizer = sr.Recognizer()

  with sr.Microphone() as audio_source:
    recognizer.adjust_for_ambient_noise(audio_source, duration=0.5)
    greet()

    # while True:
    #   listen_and_respond(audio_source, recognizer)


# def listen_and_respond(audio_source, recognizer):
#   audio = recognizer.listen(audio_source)

#   try:
#     transcription = recognizer.recognize_google(audio)
#     print(transcription)  # TODO
#   except sr.UnknownValueError:
#     print("error")  # TODO


if __name__ == "__main__":
  run_weather_bot()
