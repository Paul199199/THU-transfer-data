import csv
f = 'student.csv'
with open(f,'a',encoding='UTF-8')as fo:#,newline=''可加入這行讓中間不要有段行
    csvWriter = csv.writer(fo)
    csvWriter.writerow(['姓名','系別','性別'])
    csvWriter.writerow(['朱伊文','資工系','男'])
    csvWriter.writerow(['陳子涵','企管系','女'])