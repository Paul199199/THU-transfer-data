import sqlite3
conn = sqlite3.connect('lcc.db')
sql = 'create table if not exists bike(id integer primary key autoincrement,station varchar(30),rent int,space int)'

conn.execute(sql)
conn.commit()
conn.close()