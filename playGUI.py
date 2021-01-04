from tkinter import *
from audioplayer import AudioPlayer
from tkinter import filedialog

root = Tk()
root.title('Music Player')
root.configure(bg='light blue')
root.option_add('*tearOff',False)
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
menubar.add_cascade(menu= file, label='File')
file.add_command(label='Add Song',
                 command = lambda: filedialog.askopenfile())
file.add_command(label='Delete Song',
                 command = lambda:print('Deleting song...'))
file.add_command(label='Exit', command = lambda: root.destroy())


root.mainloop() 

