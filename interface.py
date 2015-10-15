__author__ = 'junqi'
import Tkinter as tk
import os,collections,filter,glob,interface2

class MainWindow(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Parser LAS files to .csv files", command=self.LAStoCSV)
        self.button.pack(side="top")
        self.button = tk.Button(self, text="GenerateReport", command=self.Report)
        self.button.pack(side="top")
        self.button = tk.Button(self, text="Begin Filter", command=self.create_window)
        self.button.pack(side="top")
        self.button = tk.Button(self, text="close", command=root.destroy)
        self.button.pack(side="top")

    def LAStoCSV(self):
        execfile("readLAS.py")

    def Report(self):
        execfile("datareport.py")

    def create_window(self):
        t = tk.Toplevel(self)
        win1 = Win1(t)
        win1.pack(side = "top")

class Win1(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Show Data by Data frequency", command=self.frequency)
        self.button.pack(side="top")
        self.button = tk.Button(self, text="Show Data by Data alphabet", command=self.alphabet)
        self.button.pack(side="top")
        self.button = tk.Button(self, text="More Filters", command=self.advance)
        self.button.pack(side="top")

    def advance(self):
        t = tk.Toplevel(self)
        t.b = tk.Button(t, text="close", command=lambda: t.destroy())
        t.b.pack()
        win3 = interface2.Win3(t)
        win3.pack(side = "top")

    def frequency(self):
        all_result = glob.glob('filter/*.csv')
        for files in all_result:
            os.remove(files)

        freq = dict()
        with open("report/columnreport.txt") as f:
            content = [x.strip('\n') for x in f.readlines()]
            for item in content:
                l = item.split(":")
                item = l[0]+":"+l[1]+":"+l[2]
                key = l[2]
                freq.update({int(key): item})
            freq = collections.OrderedDict(sorted(freq.items()))
        t = tk.Toplevel(self)
        t.b = tk.Button(t, text="close", command=lambda: t.destroy())
        t.b.pack()
        win2 = Win2(t, freq)
        win2.pack(side = "top")

    def alphabet(self):
        all_result = glob.glob('filter/*.csv')
        for files in all_result:
            os.remove(files)

        freq = dict()
        with open("report/columnreport.txt") as f:
            content = [x.strip('\n') for x in f.readlines()]
            for item in content:
                l = item.split(":")
                item = l[0]+":"+l[1]+":"+l[2]
                key = l[0]
                freq.update({key: item})
            freq = collections.OrderedDict(sorted(freq.items()))
        t = tk.Toplevel(self)
        t.b = tk.Button(t, text="close", command=lambda: t.destroy())
        t.b.pack()
        win2 = Win2(t, freq)
        win2.pack(side = "top")



class Win2(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, args[0], **kwargs)
        dictionary = args[1]
        self.buttonDic = dict()
        self.check = 0
        for item, key in dictionary.iteritems():
            self.buttonDic.update({key : item})
        for item, key in dictionary.iteritems():
            self.buttonDic[key] = tk.IntVar()
            self.button = tk.Checkbutton(self, text=str(key), variable=self.buttonDic[key])
            self.button.pack(side="top")
        self.button = tk.Button(self, text="Filter Files", command=self.filter)
        self.button.pack()
        self.checkbutton = tk.Checkbutton(self, text="merge all document into one?", variable=self.check)
        self.checkbutton.pack()

    def filter(self):
        result = self.show()
        filter.c_method1(result)
        print self.check
        execfile("merge.py")
        self.destroy()


    def filter2(self):
        result = self.show()
        filter.c_method2(result)
        execfile("merge.py")
        self.destroy()

    def show(self):
        result = list()
        for key, value in self.buttonDic.items():
            state = value.get()
            if state != 0:
                keyset = str(key).split(":")
                result = result + [keyset[0].replace(" ", "")]
                self.buttonDic[key].set(0)
        return result







if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()