import datetime
def writelog(msg):
    now = datetime.datetime.now()
    strdate = now.strftime('%Y%m%d')
    strtime = now.strftime('%H:%M:%S')#時間格式
    file = strdate+'.log'#附檔名
    with open(file,'a',encoding='UTF-8') as fo:
        fo.write(strtime+'|t')
        fo.write(msg+'|n')
        
try:
    data = [10,20,30]
    print(data[5])
except Exception as err:
    writelog(str(err))