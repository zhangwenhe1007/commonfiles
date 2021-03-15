#!/usr/bin/python3

def recognize():
    from wave_test import listen
    import speech_recognition as sr

    print(listen())
    recognizer = sr.Recognizer()
    listened = sr.AudioFile('listened.wav')

    with listened as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recorded = recognizer.recognize_google(audio)

    except sr.UnknownValueError:
        recorded = ("Oops! Didn't catch that")

    except sr.RequestError as e:
        recorded = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

    print(recorded, type(recorded))

    return recorded

recognize()
