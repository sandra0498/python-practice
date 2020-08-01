import pyautogui as p
import speech_recognition as SR
import pyttsx3 as ts
import time as t

variable = SR.Recognizer()

substring = 'important'
with SR.Microphone() as receiver:
    audioInput = variable.record(receiver, duration=7)

    try:
        textOutput = variable.recognize_google(audioInput)
        if substring in textOutput:
            ss = p.screenshot('screenshot.png')
            print('screenshot taken in ', t.strftime("%I:%M:%S"))



    except Exception:
        print('Did not take the screenshot!')

