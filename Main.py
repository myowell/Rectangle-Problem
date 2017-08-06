'''
Main method for the rectangle aessessment for Apprenda Inc.

This program will take the coordinates of two rectangles and determine the following:
- If one or more lines of the two rectangles intersect
- If one rectangle contains another
- If the two rectangles share any adjacent lines

@author: Michael Yowell - michael.yowell@gmail.com
'''

from classes.rectangle import Rectangle
from classes.coordinate import Coordinate
from Tkinter import *

class RectangleGUI:
    '''Class that defines a GUI for rectangle coordinate input, calculations, and drawing.'''
    top = Tk()
    resultField = Label(top)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family System -size 10 -weight bold -slant roman "  \
            "-underline 1 -overstrike 0"
        font9 = "-family System -size 10 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        self.top.geometry("1137x548+427+261")
        self.top.title("Rectangle Program")
        self.top.configure(relief="raised")
        self.top.configure(background="#2c2c2c")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="#5c5c5c")

        self.canvas = Canvas(top)
        self.canvas.place(relx=0.25, rely=0.0, relheight=0.84, relwidth=0.75)
        self.canvas.configure(background="white")
        self.canvas.configure(borderwidth="1")
        self.canvas.configure(highlightbackground="#d9d9d9")
        self.canvas.configure(highlightcolor="black")
        self.canvas.configure(insertbackground="black")
        self.canvas.configure(relief=SUNKEN)
        self.canvas.configure(selectbackground="#c4c4c4")
        self.canvas.configure(selectforeground="black")
        self.canvas.configure(width=856)

        self.rectangleOneLabel = Label(top)
        self.rectangleOneLabel.place(relx=0.0, rely=0.02, height=61, width=278)
        self.rectangleOneLabel.configure(activebackground="#1116e1")
        self.rectangleOneLabel.configure(activeforeground="white")
        self.rectangleOneLabel.configure(activeforeground="#1116e1")
        self.rectangleOneLabel.configure(background="#be0105")
        self.rectangleOneLabel.configure(borderwidth="1")
        self.rectangleOneLabel.configure(disabledforeground="#a3a3a3")
        self.rectangleOneLabel.configure(font=font10)
        self.rectangleOneLabel.configure(foreground="#ffffff")
        self.rectangleOneLabel.configure(highlightbackground="#1116e1")
        self.rectangleOneLabel.configure(highlightcolor="#1116e1")
        self.rectangleOneLabel.configure(justify=LEFT)
        self.rectangleOneLabel.configure(relief=SUNKEN)
        self.rectangleOneLabel.configure(text='''First Rectangle X, Y''')

        self.rectOneUpperLeftLabel = Label(top)
        self.rectOneUpperLeftLabel.place(relx=0.0, rely=0.15, height=31
                , width=144)
        self.rectOneUpperLeftLabel.configure(activebackground="#f9f9f9")
        self.rectOneUpperLeftLabel.configure(activeforeground="black")
        self.rectOneUpperLeftLabel.configure(background="#ee7d92")
        self.rectOneUpperLeftLabel.configure(disabledforeground="#a3a3a3")
        self.rectOneUpperLeftLabel.configure(font=font9)
        self.rectOneUpperLeftLabel.configure(foreground="#000000")
        self.rectOneUpperLeftLabel.configure(highlightbackground="#d9d9d9")
        self.rectOneUpperLeftLabel.configure(highlightcolor="black")
        self.rectOneUpperLeftLabel.configure(text='''Upper Left:''')

        self.rectOneUpperRightLabel = Label(top)
        self.rectOneUpperRightLabel.place(relx=0.0, rely=0.22, height=31
                , width=144)
        self.rectOneUpperRightLabel.configure(activebackground="#f9f9f9")
        self.rectOneUpperRightLabel.configure(activeforeground="black")
        self.rectOneUpperRightLabel.configure(background="#ee7d92")
        self.rectOneUpperRightLabel.configure(disabledforeground="#a3a3a3")
        self.rectOneUpperRightLabel.configure(font=font9)
        self.rectOneUpperRightLabel.configure(foreground="#000000")
        self.rectOneUpperRightLabel.configure(highlightbackground="#d9d9d9")
        self.rectOneUpperRightLabel.configure(highlightcolor="black")
        self.rectOneUpperRightLabel.configure(text='''Upper Right:''')

        self.rectOneBottomLeftLabel = Label(top)
        self.rectOneBottomLeftLabel.place(relx=0.0, rely=0.29, height=31
                , width=144)
        self.rectOneBottomLeftLabel.configure(activebackground="#f9f9f9")
        self.rectOneBottomLeftLabel.configure(activeforeground="black")
        self.rectOneBottomLeftLabel.configure(background="#ee7d92")
        self.rectOneBottomLeftLabel.configure(disabledforeground="#a3a3a3")
        self.rectOneBottomLeftLabel.configure(font=font9)
        self.rectOneBottomLeftLabel.configure(foreground="#000000")
        self.rectOneBottomLeftLabel.configure(highlightbackground="#d9d9d9")
        self.rectOneBottomLeftLabel.configure(highlightcolor="black")
        self.rectOneBottomLeftLabel.configure(text='''Bottom Left:''')

        self.rectOneBottomRightLabel = Label(top)
        self.rectOneBottomRightLabel.place(relx=0.0, rely=0.36, height=31
                , width=144)
        self.rectOneBottomRightLabel.configure(activebackground="#f9f9f9")
        self.rectOneBottomRightLabel.configure(activeforeground="black")
        self.rectOneBottomRightLabel.configure(background="#ee7d92")
        self.rectOneBottomRightLabel.configure(disabledforeground="#a3a3a3")
        self.rectOneBottomRightLabel.configure(font=font9)
        self.rectOneBottomRightLabel.configure(foreground="#000000")
        self.rectOneBottomRightLabel.configure(highlightbackground="#d9d9d9")
        self.rectOneBottomRightLabel.configure(highlightcolor="black")
        self.rectOneBottomRightLabel.configure(text='''Bottom Right:''')

        self.rectOneUpperLeftX = Entry(top)
        self.rectOneUpperLeftX.place(relx=0.13, rely=0.15, relheight=0.05
                , relwidth=0.05)
        self.rectOneUpperLeftX.configure(background="white")
        self.rectOneUpperLeftX.configure(disabledforeground="#a3a3a3")
        self.rectOneUpperLeftX.configure(font="TkFixedFont")
        self.rectOneUpperLeftX.configure(foreground="#000000")
        self.rectOneUpperLeftX.configure(highlightbackground="#d9d9d9")
        self.rectOneUpperLeftX.configure(highlightcolor="black")
        self.rectOneUpperLeftX.configure(insertbackground="black")
        self.rectOneUpperLeftX.configure(selectbackground="#c4c4c4")
        self.rectOneUpperLeftX.configure(selectforeground="black")

        self.rectOneUpperLeftY = Entry(top)
        self.rectOneUpperLeftY.place(relx=0.19, rely=0.15, relheight=0.05
                , relwidth=0.05)
        self.rectOneUpperLeftY.configure(background="white")
        self.rectOneUpperLeftY.configure(disabledforeground="#a3a3a3")
        self.rectOneUpperLeftY.configure(font="TkFixedFont")
        self.rectOneUpperLeftY.configure(foreground="#000000")
        self.rectOneUpperLeftY.configure(highlightbackground="#d9d9d9")
        self.rectOneUpperLeftY.configure(highlightcolor="black")
        self.rectOneUpperLeftY.configure(insertbackground="black")
        self.rectOneUpperLeftY.configure(selectbackground="#c4c4c4")
        self.rectOneUpperLeftY.configure(selectforeground="black")

        self.rectOneUpperRightX = Entry(top)
        self.rectOneUpperRightX.place(relx=0.13, rely=0.22, relheight=0.05
                , relwidth=0.05)
        self.rectOneUpperRightX.configure(background="white")
        self.rectOneUpperRightX.configure(disabledforeground="#a3a3a3")
        self.rectOneUpperRightX.configure(font="TkFixedFont")
        self.rectOneUpperRightX.configure(foreground="#000000")
        self.rectOneUpperRightX.configure(highlightbackground="#d9d9d9")
        self.rectOneUpperRightX.configure(highlightcolor="black")
        self.rectOneUpperRightX.configure(insertbackground="black")
        self.rectOneUpperRightX.configure(selectbackground="#c4c4c4")
        self.rectOneUpperRightX.configure(selectforeground="black")

        self.rectOneUpperRightY = Entry(top)
        self.rectOneUpperRightY.place(relx=0.19, rely=0.22, relheight=0.05
                , relwidth=0.05)
        self.rectOneUpperRightY.configure(background="white")
        self.rectOneUpperRightY.configure(disabledforeground="#a3a3a3")
        self.rectOneUpperRightY.configure(font="TkFixedFont")
        self.rectOneUpperRightY.configure(foreground="#000000")
        self.rectOneUpperRightY.configure(highlightbackground="#d9d9d9")
        self.rectOneUpperRightY.configure(highlightcolor="black")
        self.rectOneUpperRightY.configure(insertbackground="black")
        self.rectOneUpperRightY.configure(selectbackground="#c4c4c4")
        self.rectOneUpperRightY.configure(selectforeground="black")

        self.rectOneBottomLeftX = Entry(top)
        self.rectOneBottomLeftX.place(relx=0.13, rely=0.29, relheight=0.05
                , relwidth=0.05)
        self.rectOneBottomLeftX.configure(background="white")
        self.rectOneBottomLeftX.configure(disabledforeground="#a3a3a3")
        self.rectOneBottomLeftX.configure(font="TkFixedFont")
        self.rectOneBottomLeftX.configure(foreground="#000000")
        self.rectOneBottomLeftX.configure(highlightbackground="#d9d9d9")
        self.rectOneBottomLeftX.configure(highlightcolor="black")
        self.rectOneBottomLeftX.configure(insertbackground="black")
        self.rectOneBottomLeftX.configure(selectbackground="#c4c4c4")
        self.rectOneBottomLeftX.configure(selectforeground="black")

        self.rectOneBottomLeftY = Entry(top)
        self.rectOneBottomLeftY.place(relx=0.19, rely=0.29, relheight=0.05
                , relwidth=0.05)
        self.rectOneBottomLeftY.configure(background="white")
        self.rectOneBottomLeftY.configure(disabledforeground="#a3a3a3")
        self.rectOneBottomLeftY.configure(font="TkFixedFont")
        self.rectOneBottomLeftY.configure(foreground="#000000")
        self.rectOneBottomLeftY.configure(highlightbackground="#d9d9d9")
        self.rectOneBottomLeftY.configure(highlightcolor="black")
        self.rectOneBottomLeftY.configure(insertbackground="black")
        self.rectOneBottomLeftY.configure(selectbackground="#c4c4c4")
        self.rectOneBottomLeftY.configure(selectforeground="black")

        self.rectOneBottomRightX = Entry(top)
        self.rectOneBottomRightX.place(relx=0.13, rely=0.36, relheight=0.05
                , relwidth=0.05)
        self.rectOneBottomRightX.configure(background="white")
        self.rectOneBottomRightX.configure(disabledforeground="#a3a3a3")
        self.rectOneBottomRightX.configure(font="TkFixedFont")
        self.rectOneBottomRightX.configure(foreground="#000000")
        self.rectOneBottomRightX.configure(highlightbackground="#d9d9d9")
        self.rectOneBottomRightX.configure(highlightcolor="black")
        self.rectOneBottomRightX.configure(insertbackground="black")
        self.rectOneBottomRightX.configure(selectbackground="#c4c4c4")
        self.rectOneBottomRightX.configure(selectforeground="black")

        self.rectOneBottomRightY = Entry(top)
        self.rectOneBottomRightY.place(relx=0.19, rely=0.36, relheight=0.05
                , relwidth=0.05)
        self.rectOneBottomRightY.configure(background="white")
        self.rectOneBottomRightY.configure(disabledforeground="#a3a3a3")
        self.rectOneBottomRightY.configure(font="TkFixedFont")
        self.rectOneBottomRightY.configure(foreground="#000000")
        self.rectOneBottomRightY.configure(highlightbackground="#d9d9d9")
        self.rectOneBottomRightY.configure(highlightcolor="black")
        self.rectOneBottomRightY.configure(insertbackground="black")
        self.rectOneBottomRightY.configure(selectbackground="#c4c4c4")
        self.rectOneBottomRightY.configure(selectforeground="black")

        self.rectangleTwoLabel = Label(top)
        self.rectangleTwoLabel.place(relx=0.0, rely=0.44, height=61, width=278)
        self.rectangleTwoLabel.configure(activebackground="#1116e1")
        self.rectangleTwoLabel.configure(activeforeground="white")
        self.rectangleTwoLabel.configure(activeforeground="#1116e1")
        self.rectangleTwoLabel.configure(background="#1116e1")
        self.rectangleTwoLabel.configure(borderwidth="1")
        self.rectangleTwoLabel.configure(disabledforeground="#a3a3a3")
        self.rectangleTwoLabel.configure(font=font10)
        self.rectangleTwoLabel.configure(foreground="#ffffff")
        self.rectangleTwoLabel.configure(highlightbackground="#1116e1")
        self.rectangleTwoLabel.configure(highlightcolor="#1116e1")
        self.rectangleTwoLabel.configure(justify=LEFT)
        self.rectangleTwoLabel.configure(relief=SUNKEN)
        self.rectangleTwoLabel.configure(text='''Second Rectangle X, Y''')

        self.rectOneUpperLeftLabel1 = Label(top)
        self.rectOneUpperLeftLabel1.place(relx=0.0, rely=0.57, height=31
                , width=144)
        self.rectOneUpperLeftLabel1.configure(activebackground="#f9f9f9")
        self.rectOneUpperLeftLabel1.configure(activeforeground="black")
        self.rectOneUpperLeftLabel1.configure(background="#647de6")
        self.rectOneUpperLeftLabel1.configure(disabledforeground="#a3a3a3")
        self.rectOneUpperLeftLabel1.configure(font=font9)
        self.rectOneUpperLeftLabel1.configure(foreground="#000000")
        self.rectOneUpperLeftLabel1.configure(highlightbackground="#d9d9d9")
        self.rectOneUpperLeftLabel1.configure(highlightcolor="black")
        self.rectOneUpperLeftLabel1.configure(text='''Upper Left:''')

        self.rectOneUpperRightLabel1 = Label(top)
        self.rectOneUpperRightLabel1.place(relx=0.0, rely=0.64, height=31
                , width=144)
        self.rectOneUpperRightLabel1.configure(activebackground="#f9f9f9")
        self.rectOneUpperRightLabel1.configure(activeforeground="black")
        self.rectOneUpperRightLabel1.configure(background="#647de6")
        self.rectOneUpperRightLabel1.configure(disabledforeground="#a3a3a3")
        self.rectOneUpperRightLabel1.configure(font=font9)
        self.rectOneUpperRightLabel1.configure(foreground="#000000")
        self.rectOneUpperRightLabel1.configure(highlightbackground="#d9d9d9")
        self.rectOneUpperRightLabel1.configure(highlightcolor="black")
        self.rectOneUpperRightLabel1.configure(text='''Upper Right:''')

        self.rectOneBottomLeftLabel1 = Label(top)
        self.rectOneBottomLeftLabel1.place(relx=0.0, rely=0.71, height=31
                , width=144)
        self.rectOneBottomLeftLabel1.configure(activebackground="#f9f9f9")
        self.rectOneBottomLeftLabel1.configure(activeforeground="black")
        self.rectOneBottomLeftLabel1.configure(background="#647de6")
        self.rectOneBottomLeftLabel1.configure(disabledforeground="#a3a3a3")
        self.rectOneBottomLeftLabel1.configure(font=font9)
        self.rectOneBottomLeftLabel1.configure(foreground="#000000")
        self.rectOneBottomLeftLabel1.configure(highlightbackground="#d9d9d9")
        self.rectOneBottomLeftLabel1.configure(highlightcolor="black")
        self.rectOneBottomLeftLabel1.configure(text='''Bottom Left:''')

        self.rectOneBottomRightLabel1 = Label(top)
        self.rectOneBottomRightLabel1.place(relx=0.0, rely=0.78, height=31
                , width=144)
        self.rectOneBottomRightLabel1.configure(activebackground="#f9f9f9")
        self.rectOneBottomRightLabel1.configure(activeforeground="black")
        self.rectOneBottomRightLabel1.configure(background="#647de6")
        self.rectOneBottomRightLabel1.configure(disabledforeground="#a3a3a3")
        self.rectOneBottomRightLabel1.configure(font=font9)
        self.rectOneBottomRightLabel1.configure(foreground="#000000")
        self.rectOneBottomRightLabel1.configure(highlightbackground="#d9d9d9")
        self.rectOneBottomRightLabel1.configure(highlightcolor="black")
        self.rectOneBottomRightLabel1.configure(text='''Bottom Right:''')

        self.rectTwoUpperLeftX = Entry(top)
        self.rectTwoUpperLeftX.place(relx=0.13, rely=0.57, relheight=0.05
                , relwidth=0.05)
        self.rectTwoUpperLeftX.configure(background="white")
        self.rectTwoUpperLeftX.configure(disabledforeground="#a3a3a3")
        self.rectTwoUpperLeftX.configure(font="TkFixedFont")
        self.rectTwoUpperLeftX.configure(foreground="#000000")
        self.rectTwoUpperLeftX.configure(highlightbackground="#d9d9d9")
        self.rectTwoUpperLeftX.configure(highlightcolor="black")
        self.rectTwoUpperLeftX.configure(insertbackground="black")
        self.rectTwoUpperLeftX.configure(selectbackground="#c4c4c4")
        self.rectTwoUpperLeftX.configure(selectforeground="black")

        self.rectTwoUpperLeftY = Entry(top)
        self.rectTwoUpperLeftY.place(relx=0.19, rely=0.57, relheight=0.05
                , relwidth=0.05)
        self.rectTwoUpperLeftY.configure(background="white")
        self.rectTwoUpperLeftY.configure(disabledforeground="#a3a3a3")
        self.rectTwoUpperLeftY.configure(font="TkFixedFont")
        self.rectTwoUpperLeftY.configure(foreground="#000000")
        self.rectTwoUpperLeftY.configure(highlightbackground="#d9d9d9")
        self.rectTwoUpperLeftY.configure(highlightcolor="black")
        self.rectTwoUpperLeftY.configure(insertbackground="black")
        self.rectTwoUpperLeftY.configure(selectbackground="#c4c4c4")
        self.rectTwoUpperLeftY.configure(selectforeground="black")

        self.rectTwoUpperRightX = Entry(top)
        self.rectTwoUpperRightX.place(relx=0.13, rely=0.64, relheight=0.05
                , relwidth=0.05)
        self.rectTwoUpperRightX.configure(background="white")
        self.rectTwoUpperRightX.configure(disabledforeground="#a3a3a3")
        self.rectTwoUpperRightX.configure(font="TkFixedFont")
        self.rectTwoUpperRightX.configure(foreground="#000000")
        self.rectTwoUpperRightX.configure(highlightbackground="#d9d9d9")
        self.rectTwoUpperRightX.configure(highlightcolor="black")
        self.rectTwoUpperRightX.configure(insertbackground="black")
        self.rectTwoUpperRightX.configure(selectbackground="#c4c4c4")
        self.rectTwoUpperRightX.configure(selectforeground="black")

        self.rectTwoUpperRightY = Entry(top)
        self.rectTwoUpperRightY.place(relx=0.19, rely=0.64, relheight=0.05
                , relwidth=0.05)
        self.rectTwoUpperRightY.configure(background="white")
        self.rectTwoUpperRightY.configure(disabledforeground="#a3a3a3")
        self.rectTwoUpperRightY.configure(font="TkFixedFont")
        self.rectTwoUpperRightY.configure(foreground="#000000")
        self.rectTwoUpperRightY.configure(highlightbackground="#d9d9d9")
        self.rectTwoUpperRightY.configure(highlightcolor="black")
        self.rectTwoUpperRightY.configure(insertbackground="black")
        self.rectTwoUpperRightY.configure(selectbackground="#c4c4c4")
        self.rectTwoUpperRightY.configure(selectforeground="black")

        self.rectTwoBottomLeftX = Entry(top)
        self.rectTwoBottomLeftX.place(relx=0.13, rely=0.71, relheight=0.05
                , relwidth=0.05)
        self.rectTwoBottomLeftX.configure(background="white")
        self.rectTwoBottomLeftX.configure(disabledforeground="#a3a3a3")
        self.rectTwoBottomLeftX.configure(font="TkFixedFont")
        self.rectTwoBottomLeftX.configure(foreground="#000000")
        self.rectTwoBottomLeftX.configure(highlightbackground="#d9d9d9")
        self.rectTwoBottomLeftX.configure(highlightcolor="black")
        self.rectTwoBottomLeftX.configure(insertbackground="black")
        self.rectTwoBottomLeftX.configure(selectbackground="#c4c4c4")
        self.rectTwoBottomLeftX.configure(selectforeground="black")

        self.rectTwoBottomLeftY = Entry(top)
        self.rectTwoBottomLeftY.place(relx=0.19, rely=0.71, relheight=0.05
                , relwidth=0.05)
        self.rectTwoBottomLeftY.configure(background="white")
        self.rectTwoBottomLeftY.configure(disabledforeground="#a3a3a3")
        self.rectTwoBottomLeftY.configure(font="TkFixedFont")
        self.rectTwoBottomLeftY.configure(foreground="#000000")
        self.rectTwoBottomLeftY.configure(highlightbackground="#d9d9d9")
        self.rectTwoBottomLeftY.configure(highlightcolor="black")
        self.rectTwoBottomLeftY.configure(insertbackground="black")
        self.rectTwoBottomLeftY.configure(selectbackground="#c4c4c4")
        self.rectTwoBottomLeftY.configure(selectforeground="black")

        self.rectTwoBottomRightX = Entry(top)
        self.rectTwoBottomRightX.place(relx=0.13, rely=0.78, relheight=0.05
                , relwidth=0.05)
        self.rectTwoBottomRightX.configure(background="white")
        self.rectTwoBottomRightX.configure(disabledforeground="#a3a3a3")
        self.rectTwoBottomRightX.configure(font="TkFixedFont")
        self.rectTwoBottomRightX.configure(foreground="#000000")
        self.rectTwoBottomRightX.configure(highlightbackground="#d9d9d9")
        self.rectTwoBottomRightX.configure(highlightcolor="black")
        self.rectTwoBottomRightX.configure(insertbackground="black")
        self.rectTwoBottomRightX.configure(selectbackground="#c4c4c4")
        self.rectTwoBottomRightX.configure(selectforeground="black")

        self.rectTwoBottomRightY = Entry(top)
        self.rectTwoBottomRightY.place(relx=0.19, rely=0.78, relheight=0.05
                , relwidth=0.05)
        self.rectTwoBottomRightY.configure(background="white")
        self.rectTwoBottomRightY.configure(disabledforeground="#a3a3a3")
        self.rectTwoBottomRightY.configure(font="TkFixedFont")
        self.rectTwoBottomRightY.configure(foreground="#000000")
        self.rectTwoBottomRightY.configure(highlightbackground="#d9d9d9")
        self.rectTwoBottomRightY.configure(highlightcolor="black")
        self.rectTwoBottomRightY.configure(insertbackground="black")
        self.rectTwoBottomRightY.configure(selectbackground="#c4c4c4")
        self.rectTwoBottomRightY.configure(selectforeground="black")

        self.resultField.place(relx=0.0, rely=0.89, height=51, width=1134)
        self.resultField.configure(activebackground="#f9f9f9")
        self.resultField.configure(activeforeground="black")
        self.resultField.configure(background="#d9d9d9")
        self.resultField.configure(disabledforeground="#a3a3a3")
        self.resultField.configure(font=font9)
        self.resultField.configure(foreground="#000000")
        self.resultField.configure(highlightbackground="#d9d9d9")
        self.resultField.configure(highlightcolor="black")
        
        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.getInput,
                font="TkMenuFont",
                foreground="#000000",
                label="Draw")
        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.clearGUI,
                font="TkMenuFont",
                foreground="#000000",
                label="Clear")
        
    def startGUI(self):
        '''Begins the main GUI event handler'''
        self.top.mainloop()
        
    def getInput(self):
        '''
        Takes the input from the text boxes and validates their contents.
        Passes valid contents to the drawRectangles() method to paint the rectangles on the canvas
        Outputs whether or not the rectangles show any of the properties of containtment, adjacency, or intersection
        '''
        rectangleError = IOError("Error: Recentagle dimensions must fit definition of a well formed rectangle. See documentation.")
        outputBuffer = [];
       
        try:
            firstRectangle = Rectangle(Coordinate(int(self.rectOneUpperLeftX.get()), int(self.rectOneUpperLeftY.get())),
                                         Coordinate(int(self.rectOneUpperRightX.get()), int(self.rectOneUpperRightY.get())),
                                          Coordinate(int(self.rectOneBottomLeftX.get()), int(self.rectOneBottomLeftY.get())),
                                          Coordinate(int(self.rectOneBottomRightX.get()), int(self.rectOneBottomRightY.get())))
            
            secondRectangle = Rectangle(Coordinate(int(self.rectTwoUpperLeftX.get()), int(self.rectTwoUpperLeftY.get())),
                                         Coordinate(int(self.rectTwoUpperRightX.get()), int(self.rectTwoUpperRightY.get())),
                                          Coordinate(int(self.rectTwoBottomLeftX.get()), int(self.rectTwoBottomLeftY.get())),
                                          Coordinate(int(self.rectTwoBottomRightX.get()), int(self.rectTwoBottomRightY.get())))
            
            if not firstRectangle.isValidRectangle() or not secondRectangle.isValidRectangle():
                raise rectangleError
            else:
                self.resultField.config(text='')
                self.drawRectangles(firstRectangle, secondRectangle)
                
                if firstRectangle.rectangleIntersects(secondRectangle) == True:
                    outputBuffer.append("Rectangles Intersect")
                    
                if firstRectangle.rectangleContains(secondRectangle):
                    outputBuffer.append("Second Rectangle Contains First Rectangle")
                    
                if secondRectangle.rectangleContains(firstRectangle):
                    outputBuffer.append("First Rectangle Contains Second Rectangle")
                    
                if firstRectangle.rectangleAdjacent(secondRectangle) or secondRectangle.rectangleAdjacent(firstRectangle):
                    outputBuffer.append("Rectangles Are Adjacent")
                    
                self.resultField.config(text=', '.join(outputBuffer))
                
        except (ValueError, IOError) as e:
                self.resultField.config(text=str(e))

    def drawRectangles(self, rectOne, rectTwo):
        '''
        Takes the dimensions from the two rectangles and draws them on the canvas
        ''' 
        rectOneX1 = int(rectOne.getUpperLeft().getX())
        rectOneY1 = int(rectOne.getUpperLeft().getY())
        rectOneX2 = int(rectOne.getBottomRight().getX())
        rectOneY2 = int(rectOne.getBottomRight().getY())
        
        rectTwoX1 = int(rectTwo.getUpperLeft().getX())
        rectTwoY1 = int(rectTwo.getUpperLeft().getY())
        rectTwoX2 = int(rectTwo.getBottomRight().getX())
        rectTwoY2 = int(rectTwo.getBottomRight().getY())
        
        self.canvas.delete("all")
        self.canvas.create_rectangle(rectOneX1, rectOneY1, rectOneX2, rectOneY2, width=2, outline='red')
        self.canvas.create_rectangle(rectTwoX1, rectTwoY1, rectTwoX2, rectTwoY2, width=2, outline='blue')
        
    def clearGUI(self):
        '''
        Clears the GUI's entry fields, result label, and canvas
        '''
        self.canvas.delete("all")
        self.resultField.config(text='')
        self.rectOneUpperLeftX.delete(0, END)
        self.rectOneUpperLeftY.delete(0, END)
        self.rectOneUpperRightX.delete(0, END)
        self.rectOneUpperRightY.delete(0, END)
        self.rectOneBottomLeftX.delete(0, END)
        self.rectOneBottomLeftY.delete(0, END)
        self.rectOneBottomRightX.delete(0, END)
        self.rectOneBottomRightY.delete(0, END)
        self.rectTwoUpperLeftX.delete(0, END)
        self.rectTwoUpperLeftY.delete(0, END)
        self.rectTwoUpperRightX.delete(0, END)
        self.rectTwoUpperRightY.delete(0, END)
        self.rectTwoBottomLeftX.delete(0, END)
        self.rectTwoBottomLeftY.delete(0, END)
        self.rectTwoBottomRightX.delete(0, END)
        self.rectTwoBottomRightY.delete(0, END)

if __name__ == '__main__':
    gui = RectangleGUI()
    gui.startGUI()