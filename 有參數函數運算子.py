
def total(start,stop,sep):
    t = 0
    for i in range(start,stop,sep):
        t+= i
    return(t)#注意間隔距離 不然答案跑不出來
    
print()

# key = input('type y start')
# while key=='y':
#     s = int(input('初始值:'))
#     e = int(input('終止值:'))
#     p = int(input('間隔值:'))
#     sum = total(s,e,p)
#     print('總和:',sum)
#     key = input('按y繼續')

##區域性設定
 
# money = 99
# def display():#內部設定 專屬值
#     money = 10
#     print("函式money:",money)
# display()
# print('外部money:',money)

def go():
    global money
    money = 11#全域
    print("go的money:",money)
go()
print(money)