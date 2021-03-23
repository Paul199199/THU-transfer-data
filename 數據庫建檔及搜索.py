# student = ["John","Bill","Cherry","David","Bill"]
# ind = student.index('Bill')#此碼為查詢LIST內的數字號
# print(ind)

# ind = student.index("Bill",2)
# print(ind)

# c = student.count('Bill')
# print(c)
# c = student.count('Peter')
# print(c)

# fruits = ['apple','banana','orange','apple','cherry','apple']

# q= input('search fruits: ')
# if fruits.count(q) == 0 :
#     print("Can't found",q)
# else:
#     c=fruits.count(q)
#     ind=0
#     for i in range(c):
#         ind = fruits.index(q,ind)
#         print(ind,'location')
#         ind+=1#跑一次後 在算一次 所以+1
        #While迴圈
student = []
while True:
    st=input('type a st name(q)')
    if st == 'q':
        break
    student.append(st)
student.insert(1,'John')#insert屬插入鍵第一區為目標地,第二區為輸入名
print(student)