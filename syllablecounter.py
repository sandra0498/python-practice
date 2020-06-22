from tkinter import *

vowels = ('a', 'e', 'i', 'o', 'u')


class syllableCounter:
    def __init__(self, win):
        self.Label1 = Label(win, text='Enter the word below', fg='#00008B')
        self.Label1.place(x=50, y=50)

        self.e1 = Entry(bd=3)
        self.e1.place(x=50, y=75)

        self.button1 = Button(win, text='ENTER', fg='#8B0000')
        self.button1.place(x=80, y=100)

        self.Label2 = Label(win, text='Total amount of syllables is -->', fg='#9400D3')
        self.Label2.place(x=50, y=150)

        self.e2 = Entry()
        self.e2.place(x=200, y=150)


window = Tk()
syllable = syllableCounter(window)
window.title('Syllable Counter')
window.configure(bg='#FAEBD7')
window.geometry('200x150')
window.mainloop()
