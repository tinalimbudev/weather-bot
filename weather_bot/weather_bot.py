import os
import speech_recognition as sr

from gtts import gTTS

from common_responses import greet, beg_pardon
from dynamic_responses import respond_dynamically


def run_weather_bot():
  recognizer = sr.Recognizer()

  with sr.Microphone() as audio_source:
    recognizer.adjust_for_ambient_noise(audio_source, duration=0.5)
    greet()

    while True:  # TODO: Change?
      listen_and_respond(audio_source, recognizer)


def listen_and_respond(audio_source, recognizer):
  audio = recognizer.listen(audio_source)

  try:
    transcription = recognizer.recognize_google(audio)
    print(transcription)  # TODO
  except sr.UnknownValueError:
    beg_pardon()


if __name__ == "__main__":
  run_weather_bot()
