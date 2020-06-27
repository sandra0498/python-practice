from tkinter import *

vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # with an exception of 'y'
twoVowelSounds = ['ae', 'ee', 'oa', 'oo', 'ou', 'oi', 'ow', 'aw', 'au']

class syllable:
    def __init__(self, win):
        self.Label1 = Label(win, text='Enter the word below ', fg='#00008B')
        self.Label1.place(x=50, y=50)

        self.e1 = Entry(bd=3)
        self.e1.place(x=50, y=75)

        self.button1 = Button(win, text='ENTER', fg='#8B0000', command=self.countSyllable)
        self.button1.bind("<Button-1>", )
        self.button1.place(x=80, y=100)

        self.Label2 = Label(win, text='Total amount of syllables is -->', fg='#9400D3')
        self.Label2.place(x=50, y=150)

        self.e2 = Entry()
        self.e2.place(x=220, y=150)






    def countSyllable(self):

        if len(self.e2.get()) == 0:
            count = 0
            word = self.e1.get()
            word = word.lower()
            for letter in word:
                if letter in vowels:
                    count += 1  # determine if the word has vowels

            first = count - self.FirstRule(count, word)
            second = count - self.SecondRule(count, word)
            third = count - self.thirdRule(count, word)
            last = count - self.lastRule(count, word)

            total = count - (first + second + third + last)
            self.e2.insert(END, str(total))

        else:
            self.e2.delete(0, END)


    @staticmethod
    def FirstRule(count, word):
        # the qu rule
        if 'q' in word:
            index = word.index('q')
            if index != len(word) - 1:
                if word[index + 1] == 'u':
                    count -= 1

        return count


    @staticmethod
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

        return count

    @staticmethod
    def thirdRule(count, word):
        # this one determines what to do if there's at least
        # >> an 'e' in the word
        if 'e' in word:
            index = word.rfind('e')
            # print('the rfind of e is ', index )
            if index == len(word) - 1:  # while 'e' is @ the end of the word
                # print('enter this loop (e is @ end ) ')
                if word[index - 2] in vowels:  # if the char two spaces in front is a vowel
                    #  >> ex) kite --> 2 vowels --> b/c 'i' is 2 spaces in front
                    #   >>> of 'e' --> it removes the vowel count --> as a result, 1 syllable
                    count -= 1  # decrements the initial vowel count
                    # print('count after ', count)

            if 'es' in word:  # checks if substring is in the string
                substrIndex = word.rfind('es')  # gets the index of the rightmost side
                # print("index of 'es' is ", substrIndex)
                if substrIndex == len(word) - 2:
                    # ^^ checks if the substring is in the end
                    # print('goes into this conditional')

                    for i in range(substrIndex - 1, substrIndex - 4, -1):
                        # ^^ checks three spaces before the substring

                        if word[i] in vowels:  # if the char is a vowel
                            count -= 1  # >> decrements the vowel count

        return count


    @staticmethod
    def lastRule(count, word):
        # this rule is intended to find if there are any two vowel sounds
        for sound in twoVowelSounds:  # iterating over the list
            if sound in word:  # checking if the element is in the word
                count -= 1
        return count










window = Tk()
s = syllable(window)
window.title('Syllable Counter')
window.configure(bg='#FAEBD7')
window.geometry('200x150')
window.mainloop()
