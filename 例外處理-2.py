data = [1,2,3]
try:
    print(10 + '10')#1方法
    print(data[3])#2方法
    print(10/0)#3方法


except IndexError as ex:
    print(ex)
    print('處理A 的方式')
    
except ZeroDivisionError as err:
    print(err)
    print('處理B 的方式')

except:
    print('其他的Error')
    
print('程式執行完畢')