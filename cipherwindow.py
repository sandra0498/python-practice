from tkinter import *
from random import *

dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
              'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
              'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
              'x': 23, 'y': 24, 'z': 25}
class window:


    def __init__(self, win):
        self.label1 = Label(win, text="Enter the message you'd like to encrypt :)")
        self.label2 = Label(win, text='The encrypted message is')
        self.t1 = Entry(bd=3)
        self.button1 = Button(win, text='Enter', width= 15, command=self.checkString())
        self.label1.place(x=100, y=50)
        self.t1.place(x=335, y=50)
        self.button1.place(x=340, y=75)



    def checkString(self):
        word = self.t1.get()
        word = word.lower()
        key = randint(1, 11)
        encrypted = self.cipher(word, key)


    @staticmethod
    def cipher(name, key):
        result = ""
        splits = name.split()
        for word in splits:
            for letter in word:
                val = dictionary.get(letter)
                val += key
                if val > 25:
                    val %= 26

                result += get_key(val)
            result += " "
        return result

    # gets the key from the value
    def get_key(val):
        for key, value in dictionary.items():
            if val == value:
                return key







cipherwindow = Tk()
ui = window(cipherwindow)
cipherwindow.title("Caesar cipher")

cipherwindow.mainloop()
