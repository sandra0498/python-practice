from tkinter import *



if __name__ == '__main__':
    window = Tk()
    window.title('Decimal Converter')
    decimal = StringVar()

    initialNum = Entry(window, textvariable=decimal)
    initialNum.grid(columnspan=4, ipadx=70)
    decimal.set('Insert decimal here')

    L1 = Label(window, text='Convert to:', font='Helvetica 12 bold')
    L1.place(x=5,y=20)
    FirstButton = Button(window, text='Hexadecimal', fg='white', bg='black', height=1, width=10)
    FirstButton.place(x=5, y=50)

    SecondButton = Button(window, text='Binary', fg='white', bg='black', height=1, width=10)
    SecondButton.place(x=5, y=80)

    window.mainloop()
