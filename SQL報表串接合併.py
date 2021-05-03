# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 21:39:35 2021

@author: user
"""

import sqlite3
conn = sqlite3.connect('lcc.db')

sql = "insert into customers(name,sex) values('王小明','男'),('陳小麗','女'),('陳比爾','男')"

conn.execute(sql)
conn.commit()

sql = "insert into orders(prices,cid) values('10000','1'),('1999','1'),('3000','3'),('8999','3')"

conn.execute(sql)
conn.commit()

sql = "select customers.name,orders.prices from customers inner join orders on customers.cid = orders.cid"
result = conn.execute(sql)

for row in result:
    print('第',row[0],'筆資料')
    print(row[1])

    print()

conn.close()