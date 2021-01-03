from tkinter import *

root = Tk()
root.option_add('*tearOff',False)
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
menubar.add_cascade(menu= file, label='File')
file.add_command(label='Add Song',
                 command = lambda:print('opening File Explorer'))
file.add_command(label='Delete Song',
                 command = lambda:print('Deleting song...'))
file.add_command(label='Exit', command = lambda: root.destroy())


root.mainloop() 
