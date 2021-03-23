# student = ['John','May',"Tom"]
# # student.remove('May')#刪除指令 挑名字

# n=student.pop(0)#刪除指令 挑數字
# print(student)
# print(n)#顯示遭刪除的名字

num1 = [1,2,3]
num2 = [4,5,6]
num3 = num1 + num2
num3.append([7,8,9])#增加一欄數字可用 __ . append
print(num3)

data = [1,2,3]
newdata = data *2 # 重複輸入運用
print(newdata)

car = ['toyota','audi','bmw','benz','honda']
print('upsidedown:',car[::-1])#顛倒順序運用
print(car)

car.reverse()
print(car)#顛倒順序運用方法2
