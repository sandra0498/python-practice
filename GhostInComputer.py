import pynput.mouse as ms
import pynput.keyboard as kb  # imported this for controlling the keyboard
import time
import os


# differentiating the two controllers
mouse = ms.Controller()
keyboard = kb.Controller()
#
# cmd = 'notepad'
# os.system(cmd)
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



for char in 'boo this is a ghost':
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)

time.sleep(5)


# needs some fixing
with keyboard.pressed(kb.Key.caps_lock):  # once the keyboard detects caps lock was pressed
    keyboard.press(kb.Key.enter)  # the enter bar is pressed
    for char in 'greetings human :)':  # a message is typed out in response
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)  # with 0.12 seconds delay in btw character



