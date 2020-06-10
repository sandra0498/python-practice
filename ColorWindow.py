from tkinter import *

class colorWindow:


    def __init__(self, win):


        self.b1 = Button(win, text= 'Red', fg= '#FF0000', command= self.turnRed)
        self.b1.place(x=100,y=50)


        self.b2 = Button(win, text = 'Yellow', fg= '#FFFF00', command= self.turnYellow)
        self.b2.place(x=130, y=50)

        self.b3 = Button(win, text = 'Green', fg ='#00FF00', command= self.turnGreen)
        self.b3.place(x=175, y=50)

        self.b4 = Button(win, text = 'Blue', fg = '#0000FF',command = self.turnBlue)
        self.b4.place(x=100, y=75)



    def turnRed(self):
        window.configure(bg = '#FF0000')

    def turnYellow(self):
        window.configure(bg= '#FFFF00')

    def turnGreen(self):
        window.configure(bg='#00FF00')

    def turnBlue(self):
        window.configure(bg='#0000FF')



window = Tk()
color = colorWindow(window)
window.title('Colors')
window.geometry('200x150')
window.mainloop()