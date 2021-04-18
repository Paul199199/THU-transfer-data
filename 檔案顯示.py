import csv
f = 'park.csv'
with open(f,encoding='UTF8')as fo:#open from f coding by UTF8
    csvReader = csv.reader(fo)#use csv open from fo
    listdata = list(csvReader)
# print(listdata)
for park in listdata:
    print(park[1])
    print(park[3])
    print(park[5])
    print()