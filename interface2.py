__author__ = 'junqi'
import Tkinter as tk
import AdvanceAction,sys

class Win3(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Replace", command=self.replace)
        self.button.pack()
        self.button = tk.Button(self, text="Filter by Range", command=self.range)
        self.button.pack()
        self.button = tk.Button(self, text="Filter by Keyword", command=self.keyword)
        self.button.pack()
        self.button = tk.Button(self, text="Sort Data")
        self.button.pack()

    def replace(self):
        a = tk.Toplevel(self)
        win_R = Replace(a)
        win_R.pack(side = "top")

    def range(self):
        a = tk.Toplevel(self)
        win_R = Range(a)
        win_R.pack(side = "top")
		
    def keyword(self):
        a = tk.Toplevel(self)
        win_R = Keyword(a)
        win_R.pack(side = "top")


class Replace(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.L1 = tk.Label(self, text="Replace")
        self.L1.pack()
        self.E1 = tk.Entry(self, bd=5)
        self.E1.pack()
        self.L1 = tk.Label(self, text="To")
        self.L1.pack()
        self.E2 = tk.Entry(self, bd=5)
        self.E2.pack()
        self.button = tk.Button(self, text="Filter",command=self.act)
        self.button.pack()

    def act(self):
        replace = self.E1.get()
        print replace
        target = self.E2.get()
        print target
        AdvanceAction.replace(replace,target)


class Range(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        content = list()
        with open('tmp.txt', 'r') as content_file:
            content = content_file.read()

        self.valid_column = str(content).split(" ")
        self.valid_column.remove('')
        self.buttonDic = dict()
        self.Elist1={}
        self.Elist2={}
        self.buttonDic={}
        for item in self.valid_column:
            self.row = tk.Frame(self)
            self.row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            var = tk.IntVar()
            self.CB = tk.Checkbutton(self.row, text=item,variable=var)
            self.buttonDic[item]= var
            self.CB.pack(side=tk.LEFT)
            self.E1 = tk.Entry(self.row)
            self.E1.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            self.Elist1[item]=self.E1
            self.lab = tk.Label(self.row, text="<= DATA <=")
            self.lab.pack(side=tk.RIGHT)
            self.E2 = tk.Entry(self.row)
            self.E2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            self.Elist2[item] = self.E2

        self.button = tk.Button(self, text="Filter", command=self.act)
        self.button.pack(side=tk.BOTTOM)

    def act(self):
        keyword=list()
        small=list()
        large=list()
        for item in self.valid_column:
            if self.buttonDic[item].get() == 1:
                keyword += [item]
                if self.Elist2[item].get() == '':
                    small += [0]
                else:
                    small += [float(self.Elist2[item].get())]
                if self.Elist1[item].get() == '':
                    large += [float("inf")]
                else:
                    large += [float(self.Elist1[item].get())]
        print small
        print large
        print keyword
        AdvanceAction.rangefile(keyword,small,large)
		

class Keyword(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        with open('filter/finalresult.csv', 'r') as content_file:
            content = content_file.read()

        valid_column = str(content).split(" ")
        valid_column.remove('')
        for item in valid_column:
            self.row = tk.Frame(self)
            self.row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            self.lab = tk.Checkbutton(self.row, text=item)
            self.lab.pack(side=tk.LEFT)
            self.E2 = tk.Entry(self.row)
            self.E2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        self.B = tk.Button(self, text="Under Construction")
        self.B.pack(side=tk.BOTTOM)