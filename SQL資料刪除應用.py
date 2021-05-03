"""
SQL刪除
此SQL新增法 編號用過之後 不補回 直接發新ID
"""

import sqlite3
conn = sqlite3.connect('lcc.db')
bid = int(input('Type a ID for Delete: '))
sql = "delete from bike where id={}".format(bid)

conn.execute(sql)
conn.commit()
        
conn.close()