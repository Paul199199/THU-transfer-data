#程式設計畫圖
# for z in range(1,10):
#     for x in range(1,z):
#         print(x,end='')
#     print()

# print('End')
#---------------------------------------------------------------------
# for z in range(1,10):
#     for x in range(1,z):
#         print(x,end='')
#     print()

# for z in range(1,10):
#     for x in range(1,x):
#         print(x,end='')
#     print()

# print('End')
#---------------------------------------------------------------------

#質數換算公式

num = int(input('type a number :'))
for i  in range(1,num+1):
    prime = 0
    for x in range(2,i):
        if i % x== 0 :
            prime = 1
    if prime == 0 :
        print(i,"是質數")