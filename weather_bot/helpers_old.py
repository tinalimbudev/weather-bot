from datetime import datetime
import os

from enum import Enum
from functools import partial
from gtts import gTTS
from pathlib import Path
from playsound import playsound
import speech_recognition as sr

from generate_audio_file import generate_audio_file_from_text


class QueryOptions(Enum):
  today = "today"
  different_day = "different day"
  current_time = "current"
  different_time = "different time"
  query_again = "yes"
  do_not_query_again = "no"
