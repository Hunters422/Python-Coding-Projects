from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(500,300) 
        self.master.maxsize(500,300)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW")
        arg = self.master


        
        self.btn_browse1 = tk.Button(self.master,width=12,height=2,text='Browse...')
        self.btn_browse1.grid(row=0,column=0,padx=(25,0),pady=(4,10),sticky=W)
        
        self.btn_browse2 = tk.Button(self.master, width=12, height=2,text='Browse...')
        self.btn_browse2.grid(row=2,column=0,padx=(25,0),pady=(4,10),sticky=W)
        
        self.btn_check = tk.Button(self.master,width=17,height=3,text='Check for Files...')
        self.btn_check.grid(row=4,column=0,padx=(25,0),pady=(4,10),sticky=W)

        self.btn_close = tk.Button(self.master, width=12, height=2,text='Close Program')
        self.btn_close.grid(row=4,column=2,padx=(25,0),pady=(4,10), sticky=SE)

        
        self.txt_browse1 = tk.Entry(self.master,text='', width=40)
        self.txt_browse1.grid(row=0,column=2,padx=(25,0),pady=(10,10),sticky=E)
        self.txt_browse2 = tk.Entry(self.master,text='', width=40)
        self.txt_browse2.grid(row=2,column=2,padx=(25,0),pady=(10,10),sticky=E)
    
        



        
        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
