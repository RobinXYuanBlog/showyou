# import tkinter as tk

# class OtherFrame(tk.Toplevel):
#     """"""
 
#     #----------------------------------------------------------------------
#     def __init__(self, original):
#         """Constructor"""
#         self.original_frame = original
#         tk.Toplevel.__init__(self)
#         self.geometry("400x300")
#         self.title("otherFrame")
 
#         btn = tk.Button(self, text="Close", command=self.onClose)
#         btn.pack()
 
#     #----------------------------------------------------------------------
#     def onClose(self):
#         """"""
#         self.destroy()
#         self.original_frame.show()
 
# ########################################################################
# class MyApp(object):
#     """"""
 
#     #----------------------------------------------------------------------
#     def __init__(self, parent):
#         """Constructor"""
#         self.root = parent
#         self.root.title("Main frame")
#         self.frame = tk.Frame(parent)
#         self.frame.pack()
 
#         btn = tk.Button(self.frame, text="Open Frame", command=self.openFrame)
#         btn.pack()
 
#     #----------------------------------------------------------------------
#     def hide(self):
#         """"""
#         self.root.withdraw()
 
#     #----------------------------------------------------------------------
#     def openFrame(self):
#         """"""
#         self.hide()
#         subFrame = OtherFrame(self)
 
#     #----------------------------------------------------------------------
#     def show(self):
#         """"""
#         self.root.update()
#         self.root.deiconify()
 
# #----------------------------------------------------------------------
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x600")
#     app = MyApp(root)
#     root.mainloop()


# Using OpenCV with TkinterPython
# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import cv2
 
def select_image():
	# grab a reference to the image panels
	global panelA, panelB
 
	# open a file chooser dialog and allow the user to select an input
	# image
	path = askopenfilename()
    # ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		edged = cv2.Canny(gray, 50, 100)
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		edged = Image.fromarray(edged)
 
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		edged = ImageTk.PhotoImage(edged)
		# if the panels are None, initialize them
		if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			# while the second panel will store the edge map
			panelB = Label(image=edged)
			panelB.image = edged
			panelB.pack(side="right", padx=10, pady=10)
 
		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=edged)
			panelA.image = image
			panelB.image = edged

# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
# kick off the GUI
root.mainloop()