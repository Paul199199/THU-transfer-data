#建檔統整運用
def score(name,s1,s2,s3):
    print('St:',name)
    print('Sc:',s1,s2,s3)
    total = s1+s2+s3
    print('Total:',total)
score('Paul',95,85,70)#方法一
print()
number=[100,70,76]    #方法二(可疊代物件)因參數有三項 所以三項參數必須輸入
score('John',*number)

print()

data = {'x':80,'y':95,'z':100}#插入導物件
def student(n1,n2,n3,x,y,z):
    print(n1,x)
    print(n2,y)
    print(n3,z)
student('John','Mary','Tom',**data)
