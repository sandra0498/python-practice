from pynput.mouse import Button, Controller
import pynput.mouse as ms
import pynput.keyboard as kb  # imported this for controlling the keyboard 
import time
from random import *
from pynput import keyboard as kb2  # imported this for listener 

# differentiating the two controllers
mouse = ms.Controller()
keyboard = kb.Controller()

mouse.position = (171, 705)
mouse.click(ms.Button.left, 1)
time.sleep(3)
keyboard.type('notepad')
time.sleep(3)
# method of pressing the enter button
keyboard.press(kb.Key.enter)

# method of clicking the notepad option
# mouse.position = (95, 223)
# mouse.click(ms.Button.left, 1)

time.sleep(3)


def on_press(key):
    try:
        print(key + ' pressed')
    except AttributeError:
        print('special key ' + key)


def on_release(key):
    print(key + ' released')
    if key == kb.Key.esc:
        return False


listener = kb2.Listener(on_press=on_press, on_release=on_release)
listener.start()

for char in 'boo this is a ghost':
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)

time.sleep(5)


# needs some fixing 
if keyboard.pressed(kb.Key.caps_lock):  # once the keyboard detects caps lock was pressed
    keyboard.press(kb.Key.enter)  # the enter bar is pressed
    for char in 'greetings human :)':  # a message is typed out in response
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)  # with 0.12 seconds delay in btw character

# # clicking on the top of the notepad application
# mouse.position = (574, 251)  # will depend on where the application opens up
# time.sleep(2)
# mouse.press(ms.Button.left)
#
# for i in range(1, 10):
#
#     mouse.position = (1269, 331)
#     mouse.position = (1204, 139)
#     mouse.position = (941, 28)
#     mouse.position = (509, 33)
#     mouse.position = (245, 185)
#     mouse.position = (29, 338)
#
#
# # mouse.release(ms.Button.left)
