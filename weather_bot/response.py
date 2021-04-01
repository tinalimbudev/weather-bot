from enum import Enum


class ResponseTypes(Enum):
  ask_how_many_days = "ask_how_many_days"
  ask_how_many_hours = "ask_how_many_hours"
  ask_if_current_time = "ask_if_current_time"
  ask_if_query_again = "ask_if_query_again"
  ask_if_today = "ask_if_today"
  ask_name = "ask_name"
  goodbye = "goodbye"
  hello = "hello"
  invalid_input = "invalid_input"
  pardon = "pardon"


RESPONSE_FILES = {
  ResponseTypes.ask_how_many_days: "ask_how_many_days.mp3",
  ResponseTypes.ask_how_many_hours: "ask_how_many_hours.mp3",
  ResponseTypes.ask_if_current_time: "ask_if_current_time.mp3",
  ResponseTypes.ask_if_query_again: "ask_if_query_again.mp3",
  ResponseTypes.ask_if_today: "ask_if_today.mp3",
  ResponseTypes.ask_name: "ask_name.mp3",
  ResponseTypes.goodbye: "goodbye.mp3",
  ResponseTypes.hello: "hello.mp3",
  ResponseTypes.invalid_input: "invalid_input.mp3",
  ResponseTypes.pardon: "pardon.mp3",
}


def play_common_response(response_type):
  file_path = os.path.join(
    Path().absolute(),
    "weather_bot",
    "media",
    "common_responses",
    RESPONSE_FILES[response_type],
  )
  playsound(file_path)


beg_pardon = partial(play_common_response, response_type=ResponseTypes.pardon)
flag_invalid_input = partial(
  play_common_response, response_type=ResponseTypes.invalid_input
)
say_goodbye = partial(play_common_response, response_type=ResponseTypes.goodbye)
say_hello = partial(play_common_response, response_type=ResponseTypes.hello)


def get_input(source, recognizer):
  audio = recognizer.listen(source)

  try:
    return recognizer.recognize_google(audio)
  except sr.UnknownValueError:
    beg_pardon()
    return get_input(source, recognizer)


def play_common_response_and_get_input(response_type, source, recognizer):
  play_common_response(response_type)
  return get_input(source, recognizer)


def ask_name(source, recognizer):
  return play_common_response_and_get_input(
    ResponseTypes.ask_name, source, recognizer
  )


def get_expected_input(expected_inputs, source, recognizer):
  input = get_input(source, recognizer)

  if not any([i in input for i in expected_inputs]):
    invalid_input()
    return get_expected_input(expected_inputs, source, recognizer)
  else:
    return input


def play_common_response_and_get_expected_input(
  response_type, expected_inputs, source, recognizer
):
  play_common_response(response_type)
  return get_expected_input(expected_inputs, source, recognizer)


def ask_if_today_or_different_day(source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_if_today,
    #[QueryOptions.today.value, QueryOptions.different_day.value],
    source,
    recognizer,
  )


def ask_if_current_time_or_different(source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_if_current_time,
    # [QueryOptions.current_time.value, QueryOptions.different_time.value],
    source,
    recognizer,
  )


def ask_how_many_hours(source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_how_many_hours,
    [str(i) for i in range(1, 13)],
    source,
    recognizer,
  )


def ask_how_many_days(source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_how_many_days,
    [str(i) for i in range(1, 8)],
    source,
    recognizer,
  )


def ask_if_query_again(source, recognizer):
  return play_common_response_and_get_expected_input(
    ResponseTypes.ask_if_query_again,
    # [QueryOptions.query_again.value, QueryOptions.do_not_query_again.value],
    source,
    recognizer,
  )
