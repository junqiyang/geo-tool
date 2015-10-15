__author__ = 'junqi'
import csv,glob
report = open("report/columnreport.txt", 'w')
columncount = dict()
rowcount = dict()

with open('result/sectionC.csv','r') as f:
    reader = csv.reader(f)
    setcolumn = next(reader)

for item in setcolumn:
    columncount.update({item: 0})
    rowcount.update({item: 0})

all_result = glob.glob('result/*.csv')
counter = 0
for files in all_result:
    if files == 'result\\finalresult.csv' or files == 'result\\sectionC.csv':
        print "skipped"
        continue
    else:
        counter += 1
        fin = open(files, 'r')
        reader = csv.reader(fin)
        checkcolumn = reader.next()
        columnindex = list()
        columnindex2 = list()
        for item in checkcolumn:
            try:
                index = setcolumn.index(item)
                index2 = checkcolumn.index(item)
                columncount[item] += 1
                columnindex = columnindex + [index]
                columnindex2 = columnindex2 + [index2]
            except KeyError:
                pass
            except ValueError:
                pass

        for line in reader:
            for i in range(0, len(columnindex)):
                element = setcolumn[columnindex[i]]
                if line[columnindex2[i]] != '':
                    rowcount[element] += 1

for item, time in columncount.iteritems():
    report.write(str(item) + '  :  ' + str(time) + ' : ' + str(rowcount[item])+ " \n")
