for i in range(1,10,3):
    print(i,end=",")
print()

for i in range(10,0,-1):
    print(i,end=",")
print()

for a in range(1,4):#range 1-3
    print("a =",a)
    for b in range(1,3):#range 1-2
        print(b,end=',')
    print()
print('system end')

for a in range(2,10):#99乘法表
    for b in range(1,10):
        print(a,'*',b,'=',a*b,sep='',end='\t')
    print()#'\t'=大空格

