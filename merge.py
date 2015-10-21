import csv,sys,glob,os

columncount = dict()
setcolumn = list()

with open('tmp.txt', 'r') as content_file:
    content = content_file.read()

valid_column = str(content).split(" ")
valid_column.remove('')


with open('result/finalresult.csv','r') as f:
    reader = csv.reader(f)
    allcolumn = next(reader)

setcolumn = list()
for item in allcolumn:
    if item == "DEPTH(F)":
        break
    setcolumn = setcolumn + [item]


for item in valid_column:
    setcolumn = setcolumn + [item]

for item in valid_column:
    if item == "DEPTH(F)":
        continue
    setcolumn = setcolumn + ['Delta_'+item]

all_result = glob.glob('filter/*.csv')
fout = open('filter/finalresult.csv','w')
writer = csv.writer(fout,lineterminator='\n')
writer.writerow(setcolumn)

line = ['']*len(setcolumn)

for files in all_result:
    print files
    if files == "filter\\finalresult.csv":
        continue
    fin = open(files, 'r')
    reader = csv.reader(fin)
    check_column = reader.next()

    indexline = ['']*len(check_column)
    for item in check_column:
        if item in setcolumn:
            indexline[check_column.index(item)] = setcolumn.index(item)
    for lines in reader:
        for i in range(len(setcolumn)):
            if i in indexline:
                index = indexline.index(i)
                try:
                    line[i] = lines[index]
                except IndexError:
                    line[i] = ''
            else:
                line[i] = ''
        writer.writerow(line)
    fin.close()
    os.remove(files)






