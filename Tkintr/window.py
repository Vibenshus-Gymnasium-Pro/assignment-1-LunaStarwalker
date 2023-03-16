from tkinter import *
from calculator import Calculator


class Window:
    def __init__(self):
        self.root = Tk()
        self.calculator = Calculator(self.root)
        self.setup()

    def donothing(self):
        pass

    def setup(self):
        self.root.title("Calculator")
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="View History", command=self.calculator.history.print)
        filemenu.add_command(label="Save History", command=self.calculator.history.save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)
        self.root.mainloop()
