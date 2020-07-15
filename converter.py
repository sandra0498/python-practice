from tkinter import *


def convertToHex():
    # getting the entry
    num = decimal.get()
    # converting the string to an int to get the hex value
    num = int(num)
    #base 10 --> base 16
    hexrep = hex(num)
    # setting the new value to the entry box
    decimal.set(str(hexrep))


if __name__ == '__main__':
    window = Tk()
    window.title('Number System Converter')
    decimal = StringVar()

    initialNum = Entry(window, textvariable=decimal)
    initialNum.grid(columnspan=4, ipadx=70)
    decimal.set('Insert value here')

    L1 = Label(window, text='Convert to:', font='Helvetica 12 bold')
    L1.place(x=5, y=20)
    FirstButton = Button(window, text='Hexadecimal', fg='white', bg='black',
                         command=lambda: convertToHex(), height=1, width=10)
    FirstButton.place(x=5, y=50)

    SecondButton = Button(window, text='Binary', fg='white', bg='black', height=1, width=10)
    SecondButton.place(x=5, y=80)

    window.mainloop()
