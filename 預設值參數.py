#計算值參數
def total(*value):
    t = 0#不然基本上都設0
    for i in value:
        t += i#*= 此代號可變成乘法，當*=變成乘法時t需等於1
    print(value)#加這行可以變成運算數值
    return t
print(total())
print(total(10,20,30))
print(total(1,2,3,4,5,6,7,8,9,10))

