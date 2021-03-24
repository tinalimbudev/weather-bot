import os
import speech_recognition as sr

from gtts import gTTS

from common_responses import hello, beg_pardon
from dynamic_responses import greet


def run_weather_bot():
  recognizer = sr.Recognizer()

  with sr.Microphone() as audio_source:
    recognizer.adjust_for_ambient_noise(audio_source, duration=0.5)

    hello()
    name = listen_and_transcribe(audio_source, recognizer)
    greet(name)


def listen_and_transcribe(audio_source, recognizer):
  audio = recognizer.listen(audio_source)

  try:
    return recognizer.recognize_google(audio)
  except sr.UnknownValueError:
    beg_pardon()
    return listen_and_transcribe(audio_source, recognizer)


if __name__ == "__main__":
  run_weather_bot()
