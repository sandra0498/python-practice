from tkinter import *

vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # with an exception of 'y'



def FirstRule(count, word):
    # the qu rule
    if 'q' in word:
        index = word.index('q')
        if index != len(word) - 1:
            if word[index + 1] == 'u':
                count -= 1

    SecondRule(count, word)

def SecondRule(count, word):
    if 'y' in word:
        index = word.index('y')
        if index == 0:
            for i in range(1, 3):  # check two spaces after the 'y'
                if word[i] in vowels:
                    count -= 1  # decrements count for every vowel found after the 'y'
        elif word.endswith('y'):
            # option if 'y' is at the end of the word
            if word[index - 1] in vowels:  # if vowel is before the char
                count -= 1  # decrement

        else:  # conditional if 'y' is in the middle
            if word[index - 1] in vowels or word[index + 1] in vowels:
                # if a vowel is on either side of 'y'
                count -= 1
    

class syllableCounter:
    def __init__(self, win):
        self.Label1 = Label(win, text='Enter the word below', fg='#00008B')
        self.Label1.place(x=50, y=50)

        self.e1 = Entry(bd=3)
        self.e1.place(x=50, y=75)

        self.button1 = Button(win, text='ENTER', fg='#8B0000', command=self.countSyllable)
        self.button1.place(x=80, y=100)

        self.Label2 = Label(win, text='Total amount of syllables is -->', fg='#9400D3')
        self.Label2.place(x=50, y=150)

        self.e2 = Entry()
        self.e2.place(x=220, y=150)

    def countSyllable(self):
        count = 0
        word = self.e1.get()
        for letter in word:
            if letter in vowels:
                count += 1  # determine if the word has vowels
                
        FirstRule(count, word)

        
        






window = Tk()
syllable = syllableCounter(window)
window.title('Syllable Counter')
window.configure(bg='#FAEBD7')
window.geometry('200x150')
window.mainloop()
