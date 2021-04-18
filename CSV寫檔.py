import csv
f = 'member.csv'
with open(f,'a',newline='',encoding='UTF8') as fo:
    fields = ['姓名','性別','電話']
    dictWriter = csv.DictWriter(fo,fieldnames= fields)
    dictWriter.writeheader()
    dictWriter.writerow({'姓名':'陳子涵','性別':'女','電話':'0903109777'})