import speech_recognition as sr

from common_responses import hello
from dynamic_responses import greet
from transcription import listen_and_transcribe


def run_weather_bot():
  recognizer = sr.Recognizer()

  with sr.Microphone() as audio_source:
    recognizer.adjust_for_ambient_noise(audio_source, duration=0.5)

    hello()
    name = listen_and_transcribe(audio_source, recognizer)
    greet(name)


if __name__ == "__main__":
  run_weather_bot()
