# -*- coding: utf-8 -*-
"""
圖表
"""
import openpyxl
from openpyxl.chart import BarChart,Reference
wb = openpyxl.Workbook()
ws = wb.active
rows = [['','y2020','y2021',],
        ['BMW',300,153],
        ['Toyota',1500,700],
        ['Audi',730,415],]
for r in rows:
    ws.append(r)
    
chart = BarChart()
chart.title = 'sales chart by car'
chart.x_axis.title = 'Mark'
chart.y_axis.title = 'Sales'

data = Reference(ws,min_col= 2,
                 max_col= 3,
                 min_row= 1,
                 max_row= 4)
chart.add_data(data,titles_from_data = True)

xtitle = Reference(ws,min_col= 1,#圖表資料
                   min_row= 2,
                   max_row= 4)
chart.set_categories(xtitle)
ws.add_chart(chart,'E1')
wb.save('demo4.xlsx')