import speech_recognition as sr


def get_input(source, recognizer):
  audio = recognizer.listen(source)

  try:
    return recognizer.recognize_google(audio)
  except sr.UnknownValueError:
    # TODO: beg_pardon()
    return get_input(source, recognizer)


def get_expected_input(expected_inputs, source, recognizer):
  input = get_input(source, recognizer)

  if not any([i in input for i in expected_inputs]):
    # TODO: invalid_input()
    return get_expected_input(expected_inputs, source, recognizer)
  else:
    return input
