from tkinter import *
from tkinter import filedialog
import tkinter as tk

class MainWindow(Frame):    
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(600,150) 
        self.master.maxsize(700,300)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW")
        arg = self.master
            
        self.btn_browse = tk.Button(self.master,width=12,height=2,text='Browse...',command = self.button_func)
        self.btn_browse.grid(row=10,column=0,padx=(25,0),pady=(40,10),sticky=W)

        self.txt_browse1 = tk.Entry(self.master,text='', width=40)
        self.txt_browse1.grid(row=10,column=2,padx=(25,0),pady=(40,10),sticky=E)

        self.btnCloseProg = Button(self.master, text='Close Program', width=15, height=2, command=self.close)
        self.btnCloseProg.grid(row=4, column=3, sticky=SE)


    def button_func(self):

        testing = self.txt_browse1.get()
        print(testing)

        test1 = self.txt_browse1.delete(0, END)
        print(test1)
       
        dirVariable = filedialog.askdirectory()
        self.lblMsg.config(text='Your chosen file directory:')
        self.txt_browse1.insert(0, dirVariable)
        print(self.txt_browse1.get())

    def close(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = MainWindow(root)
    root.mainloop()
