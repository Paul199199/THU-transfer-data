import csv
f = 'park.csv'
with open(f,encoding='UTF8')as fo:#open from f coding by UTF8
    csvReader = csv.reader(fo)
    for item in csvReader:
        print('Row %s ='% csvReader.line_num,item)#Row = 筆數