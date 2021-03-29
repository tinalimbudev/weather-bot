import speech_recognition as sr

from helpers import hello, ask_name, greet, ask_today_or_not, report_current_weather


def run_weather_bot():
  recognizer = sr.Recognizer()

  with sr.Microphone() as audio_source:
    recognizer.adjust_for_ambient_noise(audio_source, duration=0.5)

    hello()
    name = ask_name(audio_source, recognizer)
    greet(name)
    today_or_not = ask_today_or_not(audio_source, recognizer)

    if "today" in today_or_not:
      # if now
      report_current_weather()
      # if another time then get another time

    elif "different day" in today_or_not:
      # Get date and time and get report
      pass

    else:
      # Try to get today or a different date again.
      # try to get time again
      pass

    # Check if they want a different query
    # If not then exit


if __name__ == "__main__":
  run_weather_bot()
