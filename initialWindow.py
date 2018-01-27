import tkinter as tk
import pickle
from tkinter.messagebox import *

from toolTip import ToolTip
from signWindow import *
from mainWindow import *
from screen import *


# window = tk.Tk()
# window.title('Show You')
# window.geometry('480x320')

class Initializator(object):
    
    def __init__(self, parent):
        self.window = parent
        self.window.title('Show You')
        self.frame = tk.Frame(parent)
        self.frame.place(x=0, y=0, width=480, height=320)
        self.window.protocol("WM_DELETE_WINDOW", self.windowClose)
        self.init()

            
    def initialCanvas(self):
        
        # Set the initial position
        self.initX = 40
        self.initY = 120

        # User name block
        labelUser = tk.Label(self.frame, text='Username')
        labelUser.place(x=self.initX, y=self.initY, width=120, height=30)

        self.userEntry = tk.Entry(self.frame, show=None)
        self.userEntry.place(x=self.initX+120, y=self.initY, width=240, height=30)

        # Password block
        labelPwd = tk.Label(self.frame, text='Password')
        labelPwd.place(x=self.initX, y=self.initY+50, width=120, height=30)

        self.pwdEntry = tk.Entry(self.frame, show='*')
        self.pwdEntry.place(x=self.initX+120, y=self.initY+50, width=240, height=30)

        self.showButton = tk.Button(self.frame, text='Show', command=self.showButtonClick)
        self.showButton.place(x=self.initX+120+240, y=self.initY+50, width=60, height=30)

        self.hideButton = tk.Button(self.frame, text='Hide', command=self.hideButtonClick)
        # self.hideButton.place(x=initX+120+240, y=initY+50, width=60, height=30)
        self.hideButton.place_forget()

        # Operation block
        self.logButton = tk.Button(self.frame, text='Login', command=self.logButtonClick)
        self.logButton.place(x=self.initX+40, y=self.initY+50*2, width=120, height=30)
        self.signButton = tk.Button(self.frame, text='Sign Up', command=self.signButtonClick)
        self.signButton.place(x=self.initX+210, y=self.initY+50*2, width=120, height=30)

        self.createToolTip(self.userEntry, 'Mailbox or username')


    def showButtonClick(self):
        self.pwdEntry.config(show='')
        self.hideButton.place(x=self.initX+120+240, y=self.initY+50, width=60, height=30)
        self.showButton.place_forget()


    def hideButtonClick(self):
        self.pwdEntry.config(show='*')
        self.showButton.place(x=self.initX+120+240, y=self.initY+50, width=60, height=30)
        self.hideButton.place_forget()


    def createToolTip(self, widget, text):  
        toolTip = ToolTip(widget)  
        def enter(event):  
            toolTip.showtip(text)  
        def leave(event):  
            toolTip.hidetip()  
        widget.bind('<Enter>', enter)  
        widget.bind('<Leave>', leave) 


    def hide(self):
        self.window.withdraw()


    def signButtonClick(self):
        self.hide()
        sign = SignUp(self)


    def logButtonClick(self):
        userName = self.userEntry.get()
        password = self.pwdEntry.get()
        if userName == 'Robin' and password == '123':
            self.hide()
            log = MainWindow(self)
        elif userName == '' or password == '':
            tk.messagebox.showerror("Error", "No user name or password!")
        else:
            tk.messagebox.showerror("Error", "User name or password is invalid!")
            self.pwdEntry.delete(0, tk.END)
            
        # log = MainWindow()

    def show(self):
        self.window.update()
        self.window.deiconify()


    def init(self):
        self.initialCanvas()
        # self.setWindow(self.window, 480, 320)
        Screen.setWindow(self.window, 480, 320)


    def windowClose(self):
        if tk.messagebox.askyesno("Tip", "Exit Show You?"):
            self.window.quit()
