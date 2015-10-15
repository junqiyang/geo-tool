__author__ = 'junqi'
import csv,sys,glob,os

all_result = glob.glob('filter/*.csv')


def replace(a, b):
    for files in all_result:
        print files
        fin = open(files, 'r')
        fout = open(str(files)[:-4]+"0.csv",'w')
        reader = csv.reader(fin)
        writer = csv.writer(fout, lineterminator='\n')
        line = reader.next()
        writer.writerow(line)
        for line in reader:
            for i in range(len(line)):
                if line[i] == a:
                    line[i] = b
            writer.writerow(line)
        fin.close()


def rangefile(keyword=list(), small=list(), large=list()):
    for files in all_result:
        print files
        fin = open(files, 'r')
        fout = open(str(files)[:-4]+"0.csv",'w')
        reader = csv.reader(fin)
        writer = csv.writer(fout, lineterminator='\n')
        line = reader.next()
        indexlist = list()
        writer.writerow(line)

        for i in range(len(keyword)):
             index = line.index(keyword[i])
             indexlist += [index]
        for line in reader:
             checker = True
             for i in range(len(indexlist)):
                  if float(line[indexlist[i]]) < small[i] or float(line[indexlist[i]]) > large[i]:
                       checker = False
             if checker == True:
                  writer.writerow(line)
             else:
                  continue
        fin.close()


