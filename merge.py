import csv,sys,glob,os

columncount = dict()
setcolumn = list()

with open('tmp.txt', 'r') as content_file:
    content = content_file.read()

valid_column = str(content).split(" ")
valid_column.remove('')
print valid_column

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

check = True
for item in allcolumn:

    if item == 'ELEVATION OF KELLY BUSHING':
        check = False
    if check == False:
        setcolumn = setcolumn + [item]
    else:
        continue

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
        for i in range(0, len(setcolumn)-1):
            if i in indexline:
                index = indexline.index(i)
                line[i] = lines[index]
            else:
                line[i] = ''
        writer.writerow(line)
    fin.close()
    os.remove(files)






