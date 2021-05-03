"""
SQL資料串接合併
"""

import sqlite3
conn = sqlite3.connect('lcc.db')
sql = "create table if not exists customers(cid integer primary key autoincrement,name varchar(30),sex varchar(2))"

conn.execute(sql)
conn.commit()

sql = "create table if not exists orders(id integer primary key autoincrement,prices int, cid int)"

conn.execute(sql)
conn.commit()

conn.close()