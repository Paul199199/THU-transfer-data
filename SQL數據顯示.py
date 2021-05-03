import sqlite3
conn = sqlite3.connect('lcc.db')
sql = 'select * from bike'
result = conn.execute(sql)
#方法一
# data = list(result)
# print(data)

#方法二
for row in result:
    print('第',row[0],'筆資料')
    print(row[1])
    print(row[2])
    print(row[3])
    print()
    
# print(data)

conn.commit()
conn.close()
