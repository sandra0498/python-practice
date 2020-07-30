import speech_recognition as SR
import time as t
import pyttsx3 as ts

engine = ts.init()

variable = SR.Recognizer()

with SR.Microphone() as source:
    print('speak now...')
    audioInput = variable.record(source, duration=7)

    try:
        textOutput = variable.recognize_google(audioInput)
        print('text converted from audio: \n')
        print(textOutput)
        engine.say("You said: " + textOutput)
        engine.runAndWait()
        print('Execution time: ', t.strftime("%I:%M:%S"))

    except Exception:
        print("Couldn't process the audio input ")
