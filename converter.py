from tkinter import *
import tkinter.messagebox


def convertToHex():
    # getting the entry
    num = number.get()
    try:
        # converting the string to an int to get the hex value
        num = int(num)
        # base 10 --> base 16
        hexrep = hex(num)
        # setting the new value to the entry box
        number.set(str(hexrep))
    except ValueError:
        tkinter.messagebox.showerror('Error', 'Insert digits only!')


def converttoBin():
    num = number.get()
    try:
        num = int(num)
        binRep = bin(num)
        # removes the first two characters of the binary (0x )
        binRep = binRep[2:]
        number.set(str(binRep))
    except ValueError:
        tkinter.messagebox.showerror('Error', 'Insert digits only!')






def clear():
    # setting the entry to blank
    number.set("")


if __name__ == '__main__':
    window = Tk()
    window.title('Number System Converter')
    number = StringVar()

    initialNum = Entry(window, textvariable=number)
    initialNum.grid(columnspan=4, ipadx=70)
    number.set('Insert value here')

    L1 = Label(window, text='Convert to:', font='Helvetica 12 bold')
    L1.place(x=5, y=20)
    FirstButton = Button(window, text='Hexadecimal', fg='white', bg='black',
                         command=lambda: convertToHex(), height=1, width=10)
    FirstButton.place(x=5, y=50)

    SecondButton = Button(window, text='Binary', fg='white', bg='black',
                          command=lambda: converttoBin(), height=1, width=10)
    SecondButton.place(x=5, y=80)

    clearButton = Button(window, text='Clear', fg='white', bg='black',
                         command=lambda: clear(), height=1, width=10)
    clearButton.place(x=5, y=110)

    window.mainloop()
