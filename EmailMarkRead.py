import pynput.mouse as ms
import pynput.keyboard as kb
import time

# differentiating the two controllers
mouse = ms.Controller()
keyboard = kb.Controller()

# (917, 700) -- position of the firefox icon on taskbar
mouse.position = (917, 700)
mouse.click(ms.Button.left, 1)

time.sleep(3)
keyboard.press(kb.Key.ctrl)
keyboard.press('t')

keyboard.release(kb.Key.ctrl)
keyboard.release('t')

time.sleep(3)
keyboard.type('gmail.com')
# method of pressing the enter button
keyboard.press(kb.Key.enter)

time.sleep(5)

# position of the select all box (69, 189)
mouse.position = (69, 189)
mouse.click(ms.Button.left, 1)
# position of the mark all read option -- (218, 189)
mouse.position = (218, 189)
time.sleep(2)
mouse.click(ms.Button.left, 1)  # this marks all your emails as read

time.sleep(1)
mouse.position = (69, 189)
mouse.click(ms.Button.left, 1)

