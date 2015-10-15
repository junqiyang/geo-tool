__author__ = 'junqi'
import csv, glob, os, shutil

directory = os.getcwd()
directory = directory.replace('\\', '/')
path = directory + '/result'
all_files = glob.glob(os.path.join(path, '*.csv'))


def c_method1(list1):
    fin = open("tmp.txt",'w')
    for item in list1:
        fin.write(item + " ")
    for files in all_files:
        if files == directory+'/result\\finalresult.csv' or files == directory+'/result\\sectionC.csv':
            print "skipped"
            continue

        valid = False
        fin = open(files, 'r')
        reader = csv.reader(fin)
        line = reader.next()
        for item in list1:
            if item in line:
                valid = True

        fin.close()
        if valid == True:
            files = str(files).replace('/','\\')
            path2 = directory + '/filter'
            target = str(path2).replace('/', '\\')
            os.system("xcopy /s /i %s %s " % (files, target))


def c_method2(list1):
    fin = open("tmp.txt",'w')
    for item in list1:
        fin.write(item + " ")
    for files in all_files:
        if files == directory+'/result\\finalresult.csv' or files == directory+'/result\\sectionC.csv':
            print "skipped"
            continue


        valid = True
        fin = open(files, 'r')
        reader = csv.reader(fin)
        line = reader.next()
        for item in list1:
            if item not in line:
                valid = False

        fin.close()
        if valid == True:
            print "success"
            files = str(files).replace('/','\\')
            path2 = directory + '/filter'
            target = str(path2).replace('/', '\\')
            os.system("xcopy /s /i %s %s " % (files, target))

