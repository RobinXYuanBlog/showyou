import tkinter as tk 

class Screen():

    def getScreen(window):
        width, height = window.winfo_screenwidth(),window.winfo_screenheight()
        return width, height


    def getWindow(window):
        width, height = window.winfo_reqwidth(),window.winfo_reqheight()
        return width, height


    def setWindow(root, width, height):  
        screenwidth = root.winfo_screenwidth()  
        screenheight = root.winfo_screenheight()
        root.resizable(width = False, height = False)
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
        root.geometry(size)