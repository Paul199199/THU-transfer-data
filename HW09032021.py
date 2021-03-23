#1.
123456789
12345678
1234567
123456
12345
1234
123
12
1

#2.
   *   1
  ***  3
 ***** 5
*******7
 *****
  ***
   *
   
#3.
#猜數字
import random
ans = random.randint(1,100)
guess = 0
while ans != guess :
    guess = int(input("Type a number between 1-100:"))
    if guess > ans:
        print('small')#介於多少至多少之間
    if guess < ans:
        print("biger")#介於多少至多少之間

print('bingo!')
