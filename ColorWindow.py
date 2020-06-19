from tkinter import *
from random import *


class colorWindow:

    def __init__(self, win):
        self.b1 = Button(win, text='Red', fg='#FF0000', command=self.turnRed)
        self.b1.place(x=100, y=50)

        self.b2 = Button(win, text='Yellow', fg='#FFD700', command=self.turnYellow)
        self.b2.place(x=130, y=50)

        self.b3 = Button(win, text='Green', fg='#00a86b', command=self.turnGreen)
        self.b3.place(x=175, y=50)

        self.b4 = Button(win, text='Blue', fg='#0000FF', command=self.turnBlue)
        self.b4.place(x=100, y=75)

        self.b5 = Button(win, text='Purple', fg='#800080', command=self.turnPurple)
        self.b5.place(x=130, y=75)

        self.b6 = Button(win, text='Orange', fg='#FF5733', command=self.turnOrange)
        self.b6.place(x=170, y=75)

        self.b7 = Button(win, text='Pink', fg='#FF1493', command=self.turnPink)
        self.b7.place(x=120, y=100)

        self.b8 = Button(win, text='Cyan', fg='#008080', command=self.turnCyan)
        self.b8.place(x=153, y=100)

        self.b9 = Button(win, text='Brown', fg='#52361b', command=self.turnBrown)
        self.b9.place(x=187, y=100)

        self.b10 = Button(win, text='Tan', fg='#cda776', command=self.turnTan)
        self.b10.place(x=90, y=100)

    def turnRed(self):
        colors = ['#cf352e', '#c80815', '#850505', '#9b111e', '#ff0800', '#800000', '#FF6347',
                  '#DC143C', '#DB7093', '#B22222', '#922724', '#8A0707', '#FF0000', '#800020']
        # window.configure(bg='#FF0000')

        for time in range(200, 2000, 200):  # beginning 200 ms - 2000 ms -- 200 step value
            x = randrange(len(colors))  # creates a randomly generated index from 0 to the length of the list
            window.after(time, lambda: window.configure(bg=colors[x]))
        # this  ^^ for loop ^^ takes care of the code below

        # window.configure(bg='#FF0000')
        # window.after(200, lambda: window.configure(bg='#800000'))  # maroon
        # window.after(400, lambda: window.configure(bg='#FF6347'))  # tomato
        # window.after(600, lambda: window.configure(bg='#DC143C'))  # crimson
        # window.after(800, lambda: window.configure(bg='#DB7093'))  # pale violet red
        # window.after(1000, lambda: window.configure(bg='#B22222'))  # firebrick

    def turnYellow(self):
        yellows = ['#FFFF00', '#ADFF2F', '#9ACD32', '#CCCC00', '#808000', '#FFFACD', '#fff700', '#fffe7a',
                   '#ffd800', '#f0e130', '#dfff00', '#f1ff62', '#fdde6c', '#FFD700', '#e4d00a']

        for time in range(200, 2000, 200):
            x = randrange(len(yellows))
            window.after(time, lambda: window.configure(bg=yellows[x]))
        #
        # window.configure(bg='#FFFF00')
        # window.after(200, lambda: window.configure(bg='#ADFF2F'))  # green yellow
        # window.after(400, lambda: window.configure(bg='#9ACD32'))  # yellow green
        # window.after(600, lambda: window.configure(bg='#CCCC00'))  # dark yellow 1
        # window.after(800, lambda: window.configure(bg='#808000'))  # olive
        # window.after(1000, lambda: window.configure(bg='#FFFACD'))  # lemon chiffon

    def turnGreen(self):
        greens = ['#008000', '#98FB98', '#00FA9A', '#6B8E23', '#2E8B57', '#7FFF00', '#32cd32', '#3fff00',
                  '#0bda51', '#00693e', '#76ff7a', '#5edc1f', '#00FF00', '#009000', '#00ff7f', '#77dd77', '#00a86b']

        for time in range(200, 2000, 200):
            x = randrange(len(greens))
            window.after(time, lambda: window.configure(bg=greens[x]))

        # window.configure(bg='#008000')
        # window.after(200, lambda: window.configure(bg='#98FB98'))  # pale green
        # window.after(400, lambda: window.configure(bg='#00FA9A'))  # medium spring green
        # window.after(600, lambda: window.configure(bg='#6B8E23'))  # olive drab
        # window.after(800, lambda: window.configure(bg='#2E8B57'))  # sea green
        # window.after(1000, lambda: window.configure(bg='#7FFF00'))  # chartreuse

    def turnBlue(self):
        blues = ['#0000FF', '#000080', '#00BFFF', '#1E90FF', '#B0E0E6', '#4682B4', '#6488ea',
                 '#0000AA', '#73c2fb', '#5D8AA8', '#002fa7', '#1ca9c9', '#89CFF0', '#0054b4', ' #1034a6',
                 '#00008b']
        for time in range(200, 2000, 200):
            x = randrange(len(blues))
            window.after(time, lambda: window.configure(bg=blues[x]))

        # window.configure(bg='#0000FF')
        # window.after(200, lambda: window.configure(bg='#000080'))  # navy
        # window.after(400, lambda: window.configure(bg='#00BFFF'))  # deep sky blue
        # window.after(600, lambda: window.configure(bg='#1E90FF'))  # dodger blue
        # window.after(800, lambda: window.configure(bg='#B0E0E6'))  # powder blue
        # window.after(1000, lambda: window.configure(bg='#4682B4'))  # steel blue

    def turnPurple(self):

        purples = ['#800080', '#FF00FF', '#DDA0DD', '#8A2BE2', '#EE82EE', '#BA55D3',
                   '#b284be', '#df73ff', '#880085', '#c9a0ff', '#FF66FF', '#9966cc',
                   '#720058', '#FF66FF', '#8e4785']
        for time in range(200, 2000, 200):
            x = randrange(len(purples))
            window.after(200, lambda: window.configure(bg=purples[x]))

        # window.configure(bg='#800080')
        # window.after(200, lambda: window.configure(bg='#FF00FF'))  # fuchsia
        # window.after(400, lambda: window.configure(bg='#DDA0DD'))  # plum
        # window.after(600, lambda: window.configure(bg='#8A2BE2'))  # blue violet
        # window.after(800, lambda: window.configure(bg='#EE82EE'))  # violet
        # window.after(1000, lambda: window.configure(bg='#BA55D3'))  # medium orchid

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

    def turnCyan(self):
        window.configure(bg='#00FFFF')
        window.after(200, lambda: window.configure(bg='#40E0D0'))  # turquoise
        window.after(400, lambda: window.configure(bg='#7FFFD4'))  # aquamarine
        window.after(600, lambda: window.configure(bg='#48D1CC'))  # medium turquoise
        window.after(800, lambda: window.configure(bg='#00CED1'))  # dark turquoise
        window.after(1000, lambda: window.configure(bg='#20B2AA'))  # light sea green

    def turnBrown(self):
        window.configure(bg='#52361b')
        window.after(200, lambda: window.configure(bg='#8B4513'))  # saddle brown
        window.after(400, lambda: window.configure(bg='#A0522D'))  # sienna
        window.after(600, lambda: window.configure(bg='#2b1d0e'))
        window.after(800, lambda: window.configure(bg='#b87333'))  # copper
        window.after(1000, lambda: window.configure(bg='#954535'))  # chestnut

    def turnTan(self):
        tans = ['#ecdd9a', '#c9bb8e', '#e3b778', '#e3c565', '#ebcfab',
                '#e4bf8f', '#d7b963', '#f4dbb5', '#f6e1c1', '#e6dbad', '#dac27c']

        for time in range(200, 2000, 200):
            x = randrange(len(tans))
            window.after(time, lambda: window.configure(bg=tans[x]))


window = Tk()
color = colorWindow(window)
window.title('Different Colors')
window.geometry('200x150')
window.configure(bg='#C0C0C0')
window.mainloop()
