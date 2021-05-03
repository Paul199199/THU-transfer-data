import sqlite3
conn = sqlite3.connect('lcc.db')
name = input('Station')
rent = int(input('Rent'))
space = int(input('Space'))

sql = "insert into bike(station,rent,space) values('{}',{},{})".format(name,rent,space)

conn.execute(sql)

conn.commit()

conn.close()