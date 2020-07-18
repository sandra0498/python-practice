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

mouse.position = (95, 223)
mouse.click(ms.Button.left, 1)
time.sleep(3)
for char in 'boo this is a ghost':
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)

# keyboard.type('boo')

# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))  # (1155, 40)
#
# i = 0
# while i < 3:
#     mouse.position = (1155,40)
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     mouse.position = (734, 341)
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     i+=1
#
