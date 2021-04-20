import openpyxl
wb = openpyxl.Workbook()
ws = wb.active


ws['A1']='連成電腦'

rows = [['Eng','Math','Inf'],
        [60,30,100],
        [50,98,81]]
for r in rows:
    ws.append(r)
wb.save('demo.xlsx')