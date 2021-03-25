#內部函式---取餘數
def exterfun(x,y):
    def innerfun(a,b):
        return divmod(a,b)#a=商(a//b),b=餘數(a%b)
    return innerfun(x,y)
print(exterfun(25,7))    