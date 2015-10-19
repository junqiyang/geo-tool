__author__ = 'junqi'
import csv
import Tkinter as tk

with open("filter/finalresult.csv", 'r') as files:
    fin = csv.reader(files)
    content = fin.next()


class calculation(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.varState = tk.StringVar()
        self.test = 0
        self.var1 = tk.StringVar()
        self.drop = tk.OptionMenu(self, self.var1, *content, command=self.pick)
        self.drop.pack()

    def pick(self,item):
        print item