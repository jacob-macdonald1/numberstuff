import collections as c
from tkinter import *
import tkinter.font as font


class TriangleNums:

    def __init__(self):
        self.tri_nums = []
        self.d = c.defaultdict(list)
        self.inp = int(input("Enter Index: "))
        self.lst = [i for i in range(1, self.inp + 1)]

    def generate(self):
        for j, e in enumerate(self.lst):
            counter = e
            while counter > 0:
                self.d[f"{j}"].append(counter)
                counter -= 1
            for m, w in enumerate(self.d[f"{j}"]):
                t = w
                counter2 = 0
                while t >= 1:
                    counter2 += t
                    t -= 1
                self.tri_nums.append(counter2)
        self.tri_nums = sorted(set(self.tri_nums))

    def gui(self):
        win = Tk()
        scroll = Scrollbar(win, orient='vertical')
        scroll.pack(side=RIGHT, fill='y')
        text = Text(win, height=30, width=300)
        f = font.Font(family="Times New Roman", size=40)
        for index in self.tri_nums:
            text.insert(END, str(index) + "\n")
        text['font'] = f
        scroll.config(command=text.yview)
        text.pack()
        win.mainloop()



if __name__ == "__main__":
    T = TriangleNums()
    T.generate()
    T.gui()

