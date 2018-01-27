import tkinter as tk 
import pickle
# from tkinter import messagebox
from tkinter.messagebox import *
from tkinter import ttk

from toolTip import ToolTip
from screen import *


class SignUp(tk.Toplevel):

    def __init__(self, original):
        self.original_frame = original
        tk.Toplevel.__init__(self)
        self.title('Sign Up')
        self.geometry('480x320')
        self.protocol("WM_DELETE_WINDOW", self.askQuit)
        # super().__init__() 
        self.init()

            
    def initialCanvas(self):
        
        # Set the initial position
        self.initX = 40
        self.initY = 50

        # User name block
        labelUser = tk.Label(self, text='Username')
        labelUser.place(x=self.initX, y=self.initY, width=120, height=30)

        self.userEntry = tk.Entry(self, show=None)
        self.userEntry.place(x=self.initX+120, y=self.initY, width=240, height=30)

        # Gender block
        v = tk.IntVar()
        v.set(1)
        maleRadio = tk.Radiobutton(self, variable=v, text='Male', value=1)
        maleRadio.place(x=self.initX+80, y=self.initY+50, width=120, height=30)

        femaleRadio = tk.Radiobutton(self, variable=v, text='Female', value=2)
        femaleRadio.place(x=self.initX+240, y=self.initY+50, width=120, height=30)

        # Password block
        labelPwd = tk.Label(self, text='Password')
        labelPwd.place(x=self.initX, y=self.initY+100, width=120, height=30)

        self.pwdEntry = tk.Entry(self, show='*')
        self.pwdEntry.place(x=self.initX+120, y=self.initY+100, width=240, height=30)

        labelRePwd = tk.Label(self, text='Password')
        labelRePwd.place(x=self.initX, y=self.initY+150, width=120, height=30)

        self.pwdReEntry = tk.Entry(self, show='*')
        self.pwdReEntry.place(x=self.initX+120, y=self.initY+150, width=240, height=30)

        self.showButton = tk.Button(self, text='Show', command=self.showButtonClick)
        self.showButton.place(x=self.initX+120+240, y=self.initY+150, width=60, height=30)

        self.hideButton = tk.Button(self, text='Hide', command=self.hideButtonClick)
        self.hideButton.place_forget()

        pwdValidLabel = ttk.Label(self, text='Passwords are same')
        pwdValidLabel.place_forget()

        pwdInvalidLabel = ttk.Label(self, text='Passwords are different')
        pwdInvalidLabel.place_forget()

        # if self.pwdEntry.get() == self.pwdReEntry.get():
        #     pwdValidLabel.place(x=self.initX+240, y=self.initY+180, width=120, height=30)
        #     pwdInvalidLabel.place_forget()
        # else:
        #     pwdInvalidLabel.place(x=self.initX+200, y=self.initY+180, width=180, height=30)
        #     pwdValidLabel.place_forget()
            
        # Operation block
        self.signButton = tk.Button(self, text='Sign Up')
        self.signButton.place(x=self.initX+140, y=self.initY+220, width=120, height=30)

        self.createToolTip(self.userEntry, 'Mailbox or username')
        self.createToolTip(self.pwdEntry, 'Please input your password')
        self.createToolTip(self.pwdReEntry, 'Please input your password again')


    def showButtonClick(self):
        self.pwdEntry.config(show='')
        self.pwdReEntry.config(show='')
        self.hideButton.place(x=self.initX+120+240, y=self.initY+150, width=60, height=30)
        self.showButton.place_forget()


    def hideButtonClick(self):
        self.pwdEntry.config(show='*')
        self.pwdReEntry.config(show='*')
        self.showButton.place(x=self.initX+120+240, y=self.initY+150, width=60, height=30)
        self.hideButton.place_forget()


    def createToolTip(self, widget, text):  
        toolTip = ToolTip(widget)  
        def enter(event):  
            toolTip.showtip(text)  
        def leave(event):  
            toolTip.hidetip()  
        widget.bind('<Enter>', enter)  
        widget.bind('<Leave>', leave) 


    def askQuit(self):
        if tk.messagebox.askyesno("Tip","Exit Sign Up?"):
            self.destroy()
            self.quit()
            self.original_frame.show()


    def init(self):
        self.initialCanvas()
        Screen.setWindow(self, 480, 320)
        self.mainloop()
