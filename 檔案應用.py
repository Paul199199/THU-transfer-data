f = 'yahoo.txt'
f_obj = open(f,encoding='UTF-8')#encoding=讀取編碼
data = f_obj.read()
f_obj.close()
print(data)

print()
print()
print()


"""
r = 唯獨
w = 覆蓋的寫
a = 接續的寫
"""
f = 'yahoo.txt'#簡化版本,系統自動關閉程式
with open(f,'w',encoding='UTF-8') as f_obj:
    
    #範例一
    # data = f_obj.read()
    # print(data)
    # print(data.rstrip())
    
    #範例二
    # for line in f_obj:#整行讀取，一行一行抓取
    #     print(line)
    
    #範例三
    # f_list = f_obj.readlines()
    # print(f_list)
    
    #範例四
    data = f_obj.read()#字元轉換，更改名稱
    new_data = data.replace('台灣','Taiwan')
    print(new_data)
    
    