#讀檔+抓取
import csv
f = 'park.csv'
with open(f,encoding='UTF8')as fo:
    csvReader = csv.reader(fo)
    dictReader = csv.DictReader(fo)
    for row in dictReader:
        print(row['Charge'])
        print(row['Range'])
        print()