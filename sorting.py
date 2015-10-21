__author__ = 'junqi'
import csv, glob


def findminmax(small = list() ,big = list()):
    with open('tmp.txt', 'r') as content_file:
        content = content_file.read()
    valid_column = str(content).split(" ")
    valid_column.remove('')
    files = open('filter/finalresult.csv', 'r')
    reader = csv.reader(files)

    all_c = reader.next()
    smalllist = [99999999999]*len(valid_column)
    bigllist = [0]*len(valid_column)
    indexlist = [0]*len(valid_column)
    for i in range(len(valid_column)):
        indexlist[i] = all_c.index(valid_column[i])

    for line in reader:
        for i in range(len(valid_column)):
            try:
                target = float(line[indexlist[i]])
            except ValueError:
                continue
            if target > bigllist[i]:
                bigllist[i] = target

            if target < smalllist[i]:
                smalllist[i] = target
    files.close()
    for item in smalllist:
        big.append(item)
    for item in bigllist:
        small.append(item)
