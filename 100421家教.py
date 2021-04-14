#1.
# w= int(input('type a number: '))

# for i in range(1,11):
#     w = w+1.2
#     print(w)

# #same as    
# w= int(input('type a number: '))

# for i in range(0,10):
#     w = w+1.2
#     print(w)
    
#2.
# n = int(input('type a number: '))
# f = 1
# t = 0
# for i in range(1,n+1):
#     f= f * i
#     t= t+f
# print(t)    

#same as
# n = int(input('type a number: '))
# f = 1

# for i in range(1,n+1):
#     f= f * i

# print(f)

#3.

#4-1.
# t = 0
# n = int(input('type a odd number: '))
# for i in range(1, n+1,2):
#     t = t+i
# print(t)

#4-2
# t = 0
# n = int(input('type a odd number: '))
# for i in range(1, n+1,2):
#     t = t+i

# for i in range(2,n+1,2):
#     t = t-i
# print(t)

#偶奇數判斷
# t=0
# for i in range(0,10):
#     if i % 2==0:
#         t=t-i
#         print('even')
#     else:
#         t=t+i
#         print('odd')
# print(t)

#4-3
# s = 0
# n = int(input('Type a number: '))
# for i in range(0,n+1):
#     s = s + i/n
# print(s)

# for i in range(0,5):
#     for j in range(0,i+1):
#         # for k in range(0,j-1):
#         print('*', end='')
#     print()
# for i in range(4,0,-1):
#     for j in range(0,i): 
#         print('*', end='')
#     print()

n = 5
for i in range(1,n+1):
    print(''*(n-1)+'*'*(2*i-1)+''*(n-i))