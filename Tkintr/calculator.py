from tkinter import *
import tkinter.font as font
from history import *

rows = [4, 3, 3, 3, 2, 2, 2, 1, 1, 1]
cols = [0, 0, 1, 2, 0, 1, 2, 0, 1, 2]
op = [' + ', ' - ', ' / ', ' * ']
sg = ['(', ')', '.']


class Calculator:

    def __init__(self, rt):
        self.root = rt
        self.buttonFont = font.Font(family='Helvetica', size=18, weight='bold')
        self.typing = Entry(self.root, width=30, relief=SUNKEN, borderwidth=20, font=self.buttonFont)
        self.typing.grid(row=0, column=0, columnspan=3)
        self.history = History(self.root)

        self.numbers = []
        self.operators = {}

        self.setup()

    def add_button(self, text, command, w=40, h=20):
        new_button = Button(self.root, text=str(text), relief=RAISED, borderwidth=10, font=self.buttonFont,
                            padx=w, pady=h, command=command)
        return new_button

    def clicked(self, n):
        current = self.typing.get()
        self.typing.delete(0, END)
        self.typing.insert(0, current + str(n))

    def clear(self):
        self.typing.delete(0, END)

    def delete(self):
        txt = self.typing.get()[:-1]
        self.typing.delete(0, END)
        self.typing.insert(0, txt)

    def save(self, text, res):
        txt = str(text) + " = " + str(res)

        return txt

    def calculate(self):
        exp = self.typing.get()
        try:
            res = eval(exp)
        except:
            self.typing.delete(0, END)
            self.typing.insert(0, 'There was an error. Try again.')
        else:
            self.history.add(self.save(exp, res))
            self.typing.delete(0, END)
            self.typing.insert(0, res)

    def setup(self):
        for i in range(10):
            self.numbers.append(self.add_button(i, lambda i=i: self.clicked(i)))
            self.numbers[i].grid(row=rows[i], column=cols[i])

        for i, x in enumerate(op):
            self.operators[x] = self.add_button(x, lambda x=x: self.clicked(x))
            self.operators[x].grid(row=i, column=4)

        for i, x in enumerate(sg):
            self.operators[x] = self.add_button(x, lambda x=x: self.clicked(x))
            self.operators[x].grid(row=i, column=5)

        button_clear = self.add_button("C", self.clear, w=100)
        button_clear.grid(row=4, column=1, columnspan=2)

        button_del = self.add_button("DEL", self.delete)
        button_del.grid(row=4, column=5)

        button_calc = self.add_button("=", self.calculate)
        button_calc.grid(row=4, column=4)
