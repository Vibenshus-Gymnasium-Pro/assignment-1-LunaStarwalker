from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Joe")
root.geometry("800x600")

myFont = font.Font(family='Helvetica', size=18, weight='bold')

myLabel = Label(root, text="Hello", font=myFont, bg="red", foreground="blue")
myLabel.pack()

def button_func():
    new_Label = Label(root, text="You broke the rules!", font=myFont, bg="black", foreground="yellow")
    new_Label.pack()

myButton = Button(root, text="Don't click me", font=myFont, bg="yellow", foreground="green", command=button_func)
myButton.pack()

root.mainloop()
