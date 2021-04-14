data = [1,2,3]
try:
    print(120/0)
    print(data[3])
except Exception as ex:#不管哪種結果,只要錯誤都算
    print(ex)
print('程式執行完畢')