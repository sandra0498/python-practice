from tkinter import *

vowels = ('a', 'e', 'i', 'o', 'u')


class syllableCounter:
    def __init__(self, win):
        self.Label1 = Label(win, text='Enter the word below', fg='#00008B')
        self.Label1.place(x=50, y=50)

        self.e1 = Entry(bd=3)
        self.e1.place(x=50, y=75)


window = Tk()
syllable = syllableCounter(window)
window.title('Syllable Counter')
window.configure(bg='#FAEBD7')
window.geometry('200x150')
window.mainloop()
