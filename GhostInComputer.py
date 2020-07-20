from pynput.mouse import Button, Controller
import pynput.mouse as ms
import pynput.keyboard as kb
import time


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
for char in 'boo this is a ghost':
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)

