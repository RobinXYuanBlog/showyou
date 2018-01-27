import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import cv2

from filter import *
from screen import *


class MainWindow(tk.Toplevel):
    
    def __init__(self, original):
        self.window = tk.Tk()
        self.original_frame = original
        # self.tl = tk.Toplevel
        self.window.title('Show You')
        self.window.protocol("WM_DELETE_WINDOW", self.askQuit)
        self.init()


    def setMenu(self):
        # style = ttk.Style()
        menuBar = tk.Menu(self.window)

        # File menu part
        fileMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='File', menu=fileMenu)
        fileMenu.add_command(label='Open File', accelerator='Command+O')
        fileMenu.add_command(label='Save File', accelerator='Command+S')
        fileMenu.add_command(label='Save File As', accelerator='Command+Shift+S')
        fileMenu.add_command(label='Recent Files')
        fileMenu.add_separator()
        fileMenu.add_command(label='Close Window', accelerator='Command+W')

        # Edit menu part
        editMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label='Redo', accelerator='Command+Z')
        editMenu.add_command(label='Undo', accelerator='Command+Shift+Z')
        editMenu.add_separator()
        editMenu.add_command(label='Cut', accelerator='Command+X')
        editMenu.add_command(label='Copy', accelerator='Command+C')
        editMenu.add_command(label='Paste', accelerator='Command+V')

        # Image part
        imageMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Image', menu=imageMenu)
        imageMenu.add_command(label='Gray')
        imageMenu.add_command(label='Channel')

        # Filter part
        filterMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Filter', menu=filterMenu)
        filterSub1 = tk.Menu(filterMenu)
        filterMenu.add_cascade(label='General', menu=filterSub1, underline=0)
        filterSub1.add_command(label='Snow')

        filterSub2 = tk.Menu(filterMenu)
        filterMenu.add_cascade(label='Framework', menu=filterSub2, underline=0)
        filterSub2.add_command(label='Normal Frame')
        filterSub2.add_command(label='Flower')

        # Show you part
        showMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Show', menu=showMenu)
        showMenu.add_command(label='Show You')

        # Help part
        helpMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='Help', menu=helpMenu)

        # About part
        aboutMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='About', menu=aboutMenu)
        aboutMenu.add_command(label='About Show You')

        self.window.config(menu=menuBar)


    def setToolBar(self):
        toolBar = tk.Frame(self.window, bd=1, relief=tk.RAISED)

        # fileImg = tk.BitmapImage(master=toolBar, file="/Users/robinxyuan/Documents/ImageProcess/prevchess.xbm")
        fileImg = tk.PhotoImage(master=toolBar, file="/Users/robinxyuan/Documents/ImageProcess/File.gif")
        fileButton = tk.Button(toolBar, image=fileImg, width=30, height=30, command=self.loadImage)
        fileButton.image_names = fileImg
        fileButton.pack(side=tk.LEFT, padx=2, pady=2)

        toolBar.pack(side=tk.TOP, fill=tk.X)


    def setMainCanvas(self):
        
        SIZE_OPTIONS = ['', '25%', '50%', '75%', '100%', '125%', '150%', '175%', '200%']
        # image = self.loadImage()

        self.imageCanvas = tk.LabelFrame(self.window, bd=0)
        self.imageCanvas.place(x=10, y=50, width=1010, height=700)
        self.infoBar = ttk.Frame(self.imageCanvas)
        self.infoBar.place(x=0, y=670, width=1010, height=30)
        sizeFrame = ttk.Frame(self.infoBar)
        sizeFrame.place(x=445, y=0, width=200, height=30)

        sizeDefault = tk.StringVar(sizeFrame)
        sizeDefault.set(SIZE_OPTIONS[4])

        sizeOptionButton = ttk.OptionMenu(sizeFrame, sizeDefault, *SIZE_OPTIONS)
        sizeOptionButton.pack(side=tk.LEFT, padx=0, pady=0)

        # lab = ttk.Label(self.infoBar, text='This is an info bar')
        # lab.pack(side=tk.LEFT)

        self.imageList = ttk.Frame(self.window)
        self.imageList.place(x=10, y=755, width=1010, height=95)
        label = ttk.Label(self.imageList, text='This is an image list', compound="center")
        label.pack(side=tk.LEFT)

        self.tabRegion = ttk.Frame(self.window)
        self.tabRegion.place(x=1030, y=50, width=400, height=800)

        tabControl = ttk.Notebook(self.tabRegion)

        tabGeneral = ttk.Frame(tabControl)
        tabControl.add(tabGeneral, text='General')

        tabChannel = ttk.Frame(tabControl)
        tabControl.add(tabChannel, text='Channel')

        tabText = ttk.Frame(tabControl)
        tabControl.add(tabText, text='Text')

        tabControl.pack(expand=1, fill="both")

        # Following are widgets on the General panel
        # Rotation image widget

        self.rotateAngle = tk.IntVar(tabGeneral)

        rotationFrame = ttk.Frame(master=tabGeneral)
        rotationFrame.place(x=25, y=30, width=400, height=60)

        rFromLabel = ttk.Label(master=rotationFrame, text='0')
        rFromLabel.place(x=0, y=20)

        rToLabel = ttk.Label(master=rotationFrame, text='360')
        rToLabel.place(x=270, y=20)

        rotationLabel = ttk.Label(master=rotationFrame, text='Rotate')
        rotationLabel.place(x=0, y=0)

        rotationScale = ttk.Scale(master=rotationFrame, from_=0, to=360, length=220, orient=tk.HORIZONTAL, variable=self.rotateAngle, command=self.imageRotation)
        rotationScale.place(x=35, y=20)

        # Exposure widget

        exFrame = ttk.Frame(master=tabGeneral)
        exFrame.place(x=25, y=80, width=400, height=60)

        exLabel = ttk.Label(master=exFrame, text='Exposure')
        exLabel.place(x=0, y=0)

        exFromLabel = ttk.Label(master=exFrame, text='-5')
        exFromLabel.place(x=0, y=20)

        exToLabel = ttk.Label(master=exFrame, text='+5')
        exToLabel.place(x=270, y=20)

        exScale = ttk.Scale(master=exFrame, from_=-5, to=5, length=220, orient=tk.HORIZONTAL)
        exScale.place(x=35, y=20)

        # Saturation widget
        satFrame = ttk.Frame(master=tabGeneral)
        satFrame.place(x=25, y=130, width=400, height=60)

        satLabel = ttk.Label(master=satFrame, text='Saturation')
        satLabel.place(x=0, y=0)

        satFromLabel = ttk.Label(master=satFrame, text='-10')
        satFromLabel.place(x=0, y=20)

        satToLabel = ttk.Label(master=satFrame, text='10')
        satToLabel.place(x=270, y=20)

        satScale = ttk.Scale(master=satFrame, from_=-10, to=10, length=220, orient=tk.HORIZONTAL)
        satScale.place(x=35, y=20)


        # Hue widget

        # Brightness


    def loadImage(self):
        path = askopenfilename()
        # panelImage = ttk.Label(self.imageCanvas)
        self.panelImage = None

        if len(path) > 0:
            image = cv2.imread(path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # imageShape = image.shape
            # imageWidth = imageShape[0]
            # imageHeight = imageShape[1]
            # image = cv2.resize(image, (boxWidth, boxHeight), cv2.INTER_CUBIC)
            image = self.imageResize(image)
            self.image = Image.fromarray(image)
            try: 
                self.image = ImageTk.PhotoImage(master=self.imageCanvas, image=self.image)
            except Exception as e:
                print(e)

            if self.panelImage is None:
                self.panelImage = ttk.Label(master=self.imageCanvas, image=self.image)
                self.panelImage.image_names = self.image
                self.panelImage.place(x=0, y=0, width=1010, height=680)

            else:
                self.panelImage.config(image=self.image)
                self.panelImage.image_names = self.image
                self.panelImage.place(x=0, y=0, width=1010, height=680)


    # def transExposure(self):

    def imageResize(self, img):
        boxWidth = 1010
        boxHeight = 670
        imgShape = img.shape
        imgWidth = imgShape[0]
        imgHeight = imgShape[1]
        ratio1 = 1.0*boxWidth / imgWidth
        ratio2 = 1.0*boxHeight / imgHeight
        imgRatio = min([ratio1, ratio2])
        width = int(imgWidth * imgRatio)
        height = int(imgHeight * imgRatio)
        if imgRatio < 1:
            imgResize = cv2.resize(img, (height, width), cv2.INTER_AREA)
        else:
            imgResize = img

        return imgResize


    def imageRotation(self, img):
        angle = self.rotateAngle.get()
        rotate = cv2.getRotationMatrix2D(img, angle=angle, scale=1)
        print(angle)


    def askQuit(self):
        if tk.messagebox.askyesno("Tips", "Exit Main Canvas?"):
            self.window.destroy()
            self.window.quit()
            self.original_frame.show()


    def init(self):
        width, height = Screen.getScreen(self.window)
        # self.setWindow(self.window, width, height)
        Screen.setWindow(self.window, width, height)
        self.setMenu()
        self.setToolBar()
        self.setMainCanvas()
        self.window.mainloop()

