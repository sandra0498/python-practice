import pyautogui as p
import speech_recognition as SR
import pyttsx3 as ts

variable = SR.Recognizer()

with SR.Microphone() as receiver:
    audioInput = variable.record(receiver, duration=7)

    try:
        substring = 'important'
        textOutput = variable.recognize_google(audioInput)
        if substring in textOutput:
            ss = p.screenshot('screenshot.png')
            


    except Exception:
        print('Error!')

