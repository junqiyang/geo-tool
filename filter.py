__author__ = 'junqi'
import csv, glob, os, shutil

directory = os.getcwd()
directory = directory.replace('\\', '/')
path = directory + '/result'
all_files = glob.glob(os.path.join(path, '*.csv'))


def c_method1(list1):
    fin = open("tmp.txt",'w')
    fin.write("DEPTH(F) ")
    for item in list1:
        fin.write(item + " ")
    for files in all_files:
        if files == directory+'/result\\finalresult.csv' or files == directory+'/result\\sectionC.csv':
            continue

        valid = False
        fin = open(files, 'r')
        reader = csv.reader(fin)
        line = reader.next()
        for item in list1:
            if item == "DEPTH(F)":
                continue
            if item in line:
                valid = True

        fin.close()
        if valid == True:
            files = str(files).replace('/','\\')
            target = str(files).replace('result','filter')
            fp = open(files, "r")
            fq = open(target, "w")
            fq.write(fp.read())
            fp.close()
            fq.close()



