from tkinter import *
import tkinter.font as font

numbers = []
operators = {}
HISTORY = ["Empty"]

root = Tk()
root.title("Calculator")

buttonFont = font.Font(family='Helvetica', size=18, weight='bold')

typing = Entry(root, width=30, relief=SUNKEN, borderwidth=20, font=buttonFont)
typing.grid(row=0, column=0, columnspan=3)


rows = [4, 3, 3, 3, 2, 2, 2, 1, 1, 1]
cols = [0, 0, 1, 2, 0, 1, 2, 0, 1, 2]
op = [' + ', ' - ', ' / ', ' * ']
sg = ['(', ')', '.']

def add_button(text, command, w=40, h=20):
    new_button = Button(root, text= str(text), relief=RAISED, borderwidth=10, font=buttonFont,
                        padx=w, pady=h, command=command)
    return new_button

def clicked(n):
    current = typing.get()
    typing.delete(0, END)
    typing.insert(0, current + str(n))

def clear():
    typing.delete(0, END)

def delete():
    txt = typing.get()[:-1]
    typing.delete(0, END)
    typing.insert(0, txt)

def calculate():
    exp = typing.get()
    try:
        res = eval(exp)
    except:
        typing.delete(0, END)
        typing.insert(0, 'There was an error. Try again.')
    else:
        HISTORY.append(str(exp) + ' = ' + str(res))
        typing.delete(0, END)
        typing.insert(0, res)

for i in range(10):
    numbers.append(add_button(i, lambda i=i: clicked(i)))
    numbers[i].grid(row=rows[i], column=cols[i])

for i, x in enumerate(op):
    operators[x] = add_button(x, lambda x=x: clicked(x))
    operators[x].grid(row=i, column=4)

for i, x in enumerate(sg):
    operators[x] = add_button(x, lambda x=x: clicked(x))
    operators[x].grid(row=i, column=5)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
"""filemenu.add_command(label="View History", command=donothing)
filemenu.add_command(label="Save History", command=donothing)
filemenu.add_separator()"""
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


root.config(menu=menubar)


button_clear = add_button("C", clear, w=100)
button_clear.grid(row=4, column=1, columnspan=2)

button_del = add_button("DEL", delete)
button_del.grid(row=4, column=5)

button_calc = add_button("=", calculate)
button_calc.grid(row=4, column=4)

root.mainloop()