from tkinter import *
class calculator:

    def __init__(self, win):
        self.label1 = Label(win, text='INSERT 1ST NUMBER')
        self.label2 = Label(win, text='INSERT 2ND NUMBER')
        self.label3 = Label(win, text='Result')
        self.entry1 = Entry(bd=3)
        self.entry2 = Entry()
        self.entry3 = Entry()
        self.button1 = Button(win, text='ADD')
        self.button2 = Button(win, text='SUBTRACT')
        self.button3 = Button(win, text='MULTIPLY')
        self.button4 = Button(win, text='DIVIDE')
        # placing the labels and where to insert the numbers
        self.label1.place(x=100, y=50)
        self.entry1.place(x=250, y=50)

        self.label2.place(x=100, y=100)
        self.entry2.place(x=250, y=100)

        self.bt1 = Button(win, text='ADD', command= self.addNum)
        self.bt2 = Button(win, text='SUBTRACT')
        self.bt2.bind('<Button-1>', self.SubNum)
        self.bt1.place(x=100, y=150)
        self.bt2.place(x=180, y=150)

        self.bt3 = Button(win, text='MULTIPLY', command= self.MultiplyNum)
        self.bt4 = Button(win, text='DIVIDE', command= self.divideNum)
        self.bt3.place(x=280, y=150)
        self.bt4.place(x=380, y=150)

        self.label3.place(x=100, y=200)
        self.entry3.place(x=200, y=200)





    def addNum(self):
        self.entry3.delete(0,'end')
        first = int(self.entry1.get())
        second = int(self.entry2.get())
        answer = first + second
        self.entry3.insert(END, str(answer))




    def SubNum(self, event):
        self.entry3.delete(0,'end')
        first = int(self.entry1.get())
        second = int(self.entry2.get())
        answer = first - second
        self.entry3.insert(END, str(answer))




    def MultiplyNum(self):
        self.entry3.delete(0,'end')
        first = int(self.entry1.get())
        second = int(self.entry2.get())
        answer = first * second
        self.entry3.insert(END, str(answer))




    def divideNum(self):
        self.entry3.delete(0,'end')
        first = int(self.entry1.get())
        second = int(self.entry2.get())
        answer = first // second
        self.entry3.insert(END, str(answer))














window = Tk()
gui_window = calculator(window)
window.title('Calculator')
window.geometry("400x300+10+10")
window.mainloop()