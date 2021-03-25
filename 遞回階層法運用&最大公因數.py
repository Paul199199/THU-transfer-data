#遞回階層法運用
def fun(x):
    if x <=1:
        return 1
    else:
        return x*fun(x-1)
print(fun(5))#5*f(4)==>4*f(3)==>3*f(2)==>2*f(1)得5*24=120

print()
#最大公因數
def gcd(n,m):
    if m ==0:
        return n
    else:
        return gcd(m,n%m)
print(gcd(80,170))

print()
