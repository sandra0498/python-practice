from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Survey:
    def __init__(self, master):

        self.frame_header = ttk.Frame(master)

        self.frame_header.pack()
        
        self.logo = PhotoImage(file='C:\\Users\\Sandra C\\Pictures\\nervous.gif')
        self.logo = self.logo.subsample(2,2)

        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan =2)
        ttk.Label(self.frame_header, text='Time for feedback!').grid(row=0,column=1)
        ttk.Label(self.frame_header,wraplength =350,
                  text=("You have enjoyed your free trial at getting to know me. "
                        "Please tell me what you thought about me :)")).grid(row=1,column=1)
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Name:').grid(row=0, column=0, sticky='sw')
        ttk.Label(self.frame_content, text='Phone:').grid(row = 0, column = 1, sticky='sw')
        ttk.Label(self.frame_content, text='Comments:').grid(row =2, column=0,sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width=24)
        self.entry_phone = ttk.Entry(self.frame_content, width=24)

        self.entry_name.grid(row=1, column=0)
        self.entry_phone.grid(row=1, column=1)

        self.entry_comments = Text(self.frame_content, width= 58, height = 10)
        self.entry_comments.grid(row=3, column=0, columnspan=2)

        ttk.Button(self.frame_content, text='Submit', command= self.submit).grid(row=4, column =0,sticky='e')
        ttk.Button(self.frame_content, text='Clear', command=self.clear ).grid(row=4, column = 1, sticky='w')


    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Phone: {}'.format(self.entry_phone.get()))
        print('Comments: {}'.format(self.entry_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title='Feedback', message='Feedback submitted!')
        


    def clear(self):
        self.entry_name.delete(0,'end')
        self.entry_phone.delete(0,'end')
        self.entry_comments.delete(1.0,'end')







def main():
    root = Tk()
    feedback = Survey(root)
    root.mainloop()


if __name__ =='__main__':
    main()
    



        
