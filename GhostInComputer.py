from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))  # (1155, 40)

i = 0
while i < 3:
    mouse.position = (1155,40)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = (734, 341)
    mouse.press(Button.left)
    mouse.release(Button.left)
    i+=1

