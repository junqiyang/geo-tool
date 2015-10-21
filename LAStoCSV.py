__author__ = 'junqi'

import csv,sys,glob,os

nullvalue = '-999.2500'
sections = (['V'])
dictionary = dict()


def check2(reader,writer):
    old_list = list()
    line1 = list()
    line2 = list()
    global nullvalue
    currentsection = 'v'
    for line in reader:
        if str(line[0])[0] == '#':#if it is a comment line
            continue

        if str(line[0])[0] == '~':
            newsection = str(line)[3].lower()
            global sections
            if newsection not in sections:
                sections = sections + [newsection]
                global dictionary
                dictionary.update({newsection: list()})
            if currentsection == 'c':
                for i in range(1,len(Corder)+1):
                    line2 = line2 + [Corder.get(i)]
                    line1 = line1 + ['']
                findme = line2.index('DEPTH(F)')

            currentsection = str(line[0])[1].lower()
            if currentsection == 'a':
                dictionary.update({'d': list()})
                d_list = dictionary['d']
                for i in range(2, len(Corder)+1):
                    line2 = line2 + ["Delta_"+Corder.get(i)]
                    d_list += ["Delta_"+Corder.get(i)]
                writer.writerow(line2)
                dictionary['d']=d_list
            if currentsection == 'c':
                order = 1
                DDD = 'DEPTH(F)'
                Corder = {order: DDD}
                line = reader.next()
                c_list = dictionary['c']
                if DDD not in c_list:
                    c_list = c_list + [DDD]
                    dictionary['c'] = c_list
            continue

        #for section W
        if currentsection == 'w':
            c_list = dictionary['w']
            phrase1 = str(line)
            phrase2 = str(line)
            try:
                index1 = phrase1.index(' ')
                index2 = phrase1.index(':')
                index3 = phrase1.index('.')
                index3 = phrase1.index('.')
                if phrase1[index3+1] != ' ':
                    phrase2 = phrase2[index2+1:-2]+'('+phrase1[index3+1]+')'
                else:
                    phrase2 = phrase2[index2+1:-2]
                phrase1 = phrase1[index1+1:index2]
                if phrase2 == 'UNIQUE WELL ID':
                    phrase1 = ' '+phrase1

                if phrase2 == 'NULL VALUE':
                    nullvalue = float(phrase1)
                else:
                    if phrase2 not in c_list:
                        c_list = c_list + [phrase2]
                        dictionary['w'] = c_list

                    line1 = line1 + [phrase1]
                    line2 = line2 + [phrase2]
            except ValueError:
                continue

        #for section c
        if currentsection == 'c':
            c_list = dictionary['c']
            phrase1 = str(line)
            phrase2 = str(line)
            index1 = phrase1.index(':')
            if phrase1[index1+1].isdigit():
                order = int(phrase1[index1+1:index1+3])
            else:
                order = order + 1
            phrase2 = phrase2[2:index1]
            phrase2 = phrase2.replace(" ", "")
            Corder.update({order: phrase2})
            if phrase2 not in c_list:
                c_list = c_list + [phrase2]
                dictionary['c'] = c_list


        #for section P
        if currentsection == 'p':
            c_list = dictionary['p']
            phrase1 = str(line)
            phrase2 = str(line)
            try:
                index1 = phrase1.index('.')
                index2 = phrase1.index(':')
                phrase1 = phrase1[index1+1:index2]
                phrase2 = phrase2[index2+1:-2]
                line1 = line1 + [phrase1]
                line2 = line2 + [phrase2]
                if phrase2 not in c_list:
                    c_list = c_list + [phrase2]
                    dictionary['p'] = c_list
            except ValueError:
                continue


        if currentsection == 'a':

            list3 = str(line[0]).split()
            delta_list = list()
            for i in range(0, len(list3)):
                checkvalue = float(list3[i])
                if checkvalue == nullvalue:
                    list3[i] = ''
                line1[findme+i] = str(list3[i])
            if old_list != []:
                for i in range(1, len(list3)):
                    try:
                        if list3[i] == '' or old_list[i] == '':
                            delta_list += ['']
                    except IndexError:
                            delta_list += ['']
                            continue
                    else:
                        a = float(list3[i])
                        b = float(old_list[i])
                        delta = a-b
                        delta_list += [str(delta)]
            old_list = list3
            writer.writerow(line1+delta_list)
        #write to filea'c