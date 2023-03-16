from scrollwindow import *


class History:
    def __init__(self, rt):
        self.history = []
        self.window = ScrollWindow(rt)

    def add(self, text):
        self.history.append(text)

    def print(self):
        self.window.run(self.history)

    def save(self):
        with open(r'C:\Users\Donap\Desktop\calc.txt', 'w') as fp:
            fp.write('\n'.join(self.history))