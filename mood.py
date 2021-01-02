from tkinter import *
from tkinter import ttk



        
def main():
    root = Tk()

    label = ttk.Label(root, text = 'I am tired, bruh ')
    label.pack()
    label.config(justify = CENTER)
    label.config(font=('Courier', 20, 'bold'))
    logo = PhotoImage(file = 'C:\\Users\\Sandra C\\Pictures\\sad.gif')
    label.config(image = logo)
    label.config(compound = 'top')
    
    

    

if __name__ == "__main__":
    main()
    
