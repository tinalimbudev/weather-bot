import speech_recognition as sr

from helpers import hello, ask_name, greet, ask_today_or_not


def run_weather_bot():
  recognizer = sr.Recognizer()

  with sr.Microphone() as audio_source:
    recognizer.adjust_for_ambient_noise(audio_source, duration=0.5)

    hello()
    name = ask_name(audio_source, recognizer)
    greet(name)
    today_or_not = ask_today_or_not(audio_source, recognizer)


if __name__ == "__main__":
  run_weather_bot()
