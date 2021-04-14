#例外處理
data = [1,2,3]
try:
    print(10/0)
    print(data[3])
except (IndexError,ZeroDivisionError) as ex:
    print(ex)
    
print('程式執行完畢')
