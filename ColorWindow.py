from tkinter import *


class colorWindow:

    def __init__(self, win):
        self.b1 = Button(win, text='Red', fg='#FF0000', command=self.turnRed)
        self.b1.place(x=100, y=50)

        self.b2 = Button(win, text='Yellow', fg='#FFFF00', command=self.turnYellow)
        self.b2.place(x=130, y=50)

        self.b3 = Button(win, text='Green', fg='#00FF00', command=self.turnGreen)
        self.b3.place(x=175, y=50)

        self.b4 = Button(win, text='Blue', fg='#0000FF', command=self.turnBlue)
        self.b4.place(x=100, y=75)

        self.b5 = Button(win, text='Purple', fg='#800080', command=self.turnPurple)
        self.b5.place(x=130, y=75)

        self.b6 = Button(win, text='Orange', fg='#FF5733', command=self.turnOrange)
        self.b6.place(x=170, y=75)

        self.b7 = Button(win, text='Pink', fg='#FF1493', command=self.turnPink)
        self.b7.place(x=120, y=100)


    def turnRed(self):
        window.configure(bg='#FF0000')
        window.after(200, lambda: window.configure(bg='#800000'))  # maroon
        window.after(400, lambda: window.configure(bg='#FF6347'))  # tomato
        window.after(600, lambda: window.configure(bg='#DC143C'))  # crimson
        window.after(800, lambda: window.configure(bg='#DB7093'))  # pale violet red
        window.after(1000, lambda: window.configure(bg='#B22222'))  # firebrick

    def turnYellow(self):
        window.configure(bg='#FFFF00')
        window.after(200, lambda: window.configure(bg='#ADFF2F'))  # green yellow
        window.after(400, lambda: window.configure(bg='#9ACD32'))  # yellow green
        window.after(600, lambda: window.configure(bg='#CCCC00'))  # dark yellow 1
        window.after(800, lambda: window.configure(bg='#808000'))  # olive
        window.after(1000, lambda: window.configure(bg='#FFFACD'))  # lemon chiffon


    def turnGreen(self):
        window.configure(bg='#008000')
        window.after(200, lambda: window.configure(bg='#98FB98'))  # pale green
        window.after(400, lambda: window.configure(bg='#00FA9A'))  # medium spring green
        window.after(600, lambda: window.configure(bg='#6B8E23'))  # olive drab
        window.after(800, lambda: window.configure(bg='#2E8B57'))  # sea green
        window.after(1000, lambda: window.configure(bg='#7FFF00'))  # chartreuse

    def turnBlue(self):
        window.configure(bg='#0000FF')
        window.after(200, lambda: window.configure(bg='#000080'))  # navy
        window.after(400, lambda: window.configure(bg='#00BFFF'))  # deep sky blue
        window.after(600, lambda: window.configure(bg='#1E90FF'))  # dodger blue
        window.after(800, lambda: window.configure(bg='#B0E0E6'))  # powder blue
        window.after(1000, lambda: window.configure(bg='#4682B4'))  # steel blue

    def turnPurple(self):
        window.configure(bg='#800080')
        window.after(200, lambda: window.configure(bg='#FF00FF'))  # fuchsia
        window.after(400, lambda: window.configure(bg='#DDA0DD'))  # plum
        window.after(600, lambda: window.configure(bg='#8A2BE2'))  # blue violet
        window.after(800, lambda: window.configure(bg='#EE82EE'))  # violet
        window.after(1000, lambda: window.configure(bg='#BA55D3'))  # medium orchid

    def turnOrange(self):
        window.configure(bg='#FF5733')
        window.after(200, lambda: window.configure(bg='#FFA500'))  # orange
        window.after(400, lambda: window.configure(bg='#FF8C00'))  # dark orange
        window.after(600, lambda: window.configure(bg='#FF4500'))  # orange red
        window.after(800, lambda: window.configure(bg='#FF7F50'))  # coral

    def turnPink(self):
        window.configure(bg='#FFC0CB')
        window.after(200, lambda: window.configure(bg='#FF69B4'))  # hot pink
        window.after(400, lambda: window.configure(bg='#FFB6C1'))  # light pink
        window.after(600, lambda: window.configure(bg='#FF1493'))  # deep pink
        window.after(800, lambda: window.configure(bg='#FFC0CB'))
        window.after(1000, lambda: window.configure(bg='#FF69B4'))  # hot pink



window = Tk()
color = colorWindow(window)
window.title('Colors')
window.geometry('200x150')
window.configure(bg='#C0C0C0')
window.mainloop()
