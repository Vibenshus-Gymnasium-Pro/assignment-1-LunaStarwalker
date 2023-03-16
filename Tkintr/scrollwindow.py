from tkinter import *


class ScrollWindow:

    def __init__(self, rt):
        self.child_w = Toplevel(rt)
        self.w = Label(self.child_w, text='History',
          font="100")
        self.scroll_bar = Scrollbar(self.child_w)
        self.mylist = Listbox(self.child_w,
                yscrollcommand=self.scroll_bar.set,
                selectmode=SINGLE)
        self.contents = []

    def run(self, history):
        self.contents = history
        self.child_w.geometry("150x250")
        self.w.pack()
        self.scroll_bar.pack(side=RIGHT,
                             fill=Y)

        for i, x in enumerate(self.contents):
            self.mylist.insert(END, str(i) + ": " + str(x))

        self.mylist.pack(side=LEFT, fill=BOTH)
        self.scroll_bar.config(command=self.mylist.yview)
        if len(self.contents) > 0:
            self.child_w.mainloop()
