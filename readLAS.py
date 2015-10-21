__author__ = 'junqi'

import csv,glob,os
import LAStoCSV
import Tkinter as tk
#variables
directory = os.getcwd()
directory = directory.replace('\\', '/')
path = directory + '/well'
all_files = glob.glob(os.path.join(path, '*.LAS'))
#list of sections: ~A,~C,~W in order we can keep track how many sections we have

# a column dictionary

filecount = 0
errorcount = 0
passcount = 0
errorlist = list()

resultfolder = directory + '/result'
if not os.path.exists(resultfolder):
    os.makedirs(resultfolder)

reportfolder = directory + '/report'
if not os.path.exists(reportfolder):
    os.makedirs(reportfolder)

filterfolder = directory + '/filter'
if not os.path.exists(filterfolder):
    os.makedirs(filterfolder)


for filename in all_files:
    try:
        filecount += 1
        fin = open(filename,'r')
        fout = open(directory+"/result/" + filename[-18:-4]+'.csv','w')
        reader = csv.reader(fin)
        writer = csv.writer(fout, lineterminator='\n')
        #version check first
        line = reader.next()
        if str(line) != "['~V']" and str(line) != "['~v']":
        	raise ValueError('we could not find version information')
        line = reader.next()
        phrase1 = str(line)
        index1 = phrase1.index('.')
        phrase1 = phrase1[index1+2:index1+6]
        version = float(phrase1)
        if version == 2.0:
            LAStoCSV.check2(reader, writer)
            fin.close()
            fout.close()
    except all:
        errorcount += 1
        errorlist.append(filename)

fout = open(directory+'/result/finalresult.csv','w')
writer2 = csv.writer(fout, lineterminator='\n')
setcolumn = list()
setcolumn += LAStoCSV.dictionary['w']
setcolumn += LAStoCSV.dictionary['p']
setcolumn += LAStoCSV.dictionary['c']
setcolumn += LAStoCSV.dictionary['d']
writer2.writerow(setcolumn)
fout.close()

fout = open(directory+'/result/sectionC.csv','w')
writer3 = csv.writer(fout, lineterminator='\n')
writer3.writerow(LAStoCSV.dictionary.get('c'))
passcount = filecount-errorcount
fout.close()

fout = open(directory+'/report/processor_report.txt','w')
fout.write("read %s files in total \n" % filecount)


fout.write("passed %s files \n" % passcount)
fout.write("failed %s files \n" % errorcount)
if errorcount != 0:
    fout.write("the failed files list below:")
    for item in errorlist:
        fout.write(item)
fout.close()