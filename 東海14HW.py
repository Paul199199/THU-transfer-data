# 1.
key = input("請輸入'P','R','J'其中一個字母:")

d = {"P":"Python", "R":"Ruby", "J":"Java"}

if key in d:
    print(d[key])
else:
    print("輸入有誤")

# 2.
numMap = {
    "0":"零",
    "1":"一",
    "2":"二",
    "3":"三",
    "4":"四",
    "5":"五",
    "6":"六",
    "7":"七",
    "8":"八",
    "9":"九",
    "10":"十",
    }

dayMap = {
    "Mon":"星期一",
    "Tue":"星期二",
    "Wed":"星期三",
    "Thu":"星期四",
    "Fri":"星期五",
    "Sat":"星期六",
    "Sun":"星期日",
    }

inputStr = input("請輸入 '2011.10.05 Wed' :")

inputStr = inputStr.replace(" ", ".")
inputList = inputStr.split('.')

yearIn = inputList[0] # 2011
monthIn = inputList[1] # 10
dateIn = inputList[2] # 05

year = str()
for y in yearIn:
    year += numMap[y]

month = str()
for m in monthIn:
    month += numMap[m]

date = str()
for d in dateIn:
    date += numMap[d]

print(year + "年" + month + "月" + date + "日 " + dayMap[inputList[3]])

# 3.
nums = input("請輸入'35246':")

# 不是印'*'就是印' '
# 因為雙迴圈會先由左至右、再由上到下執行
# 所以先印最高的那一排，再依序往下印
for i in range(10, -1, -1):
    for num in nums:
        if int(num) > i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 4.
a = {
"0":
'''\
 00  \
0  0 \
0  0 \
0  0 \
 00  \
''',

"1":
'''\
11   \
 1   \
 1   \
 1   \
1111 \
''',

"2":
'''\
2222 \
   2 \
 22  \
2    \
2222 \
''',

"3":
'''\
3333 \
   3 \
 333 \
   3 \
3333 \
''',

"4":
'''\
4 4  \
4 4  \
4444 \
  4  \
  *  \
''',

"5":
'''\
555  \
5    \
5555 \
   5 \
5555 \
''',

"6":
'''\
 66  \
6    \
6666 \
6  6 \
 66  \
''',

"7":
'''\
7777 \
   7 \
  7  \
 7   \
 7   \
''',

"8":
'''\
 88  \
8  8 \
 88  \
8  8 \
 88  \
''',

"9":
'''\
 99  \
9  9 \
 999 \
   9 \
 99  \
''',

    }
nbs = input('Type 2987340 :')
for i in range(5):
    for nb in nbs:    
        for j in range(5):
            print(a[nb][i*5+j],end='')
    print()

# 5.
numMap = {
"0":
'''\
 00  \
0  0 \
0  0 \
0  0 \
 00  \
''',

"1":
'''\
11   \
 1   \
 1   \
 1   \
1111 \
''',

"2":
'''\
2222 \
   2 \
 22  \
2    \
2222 \
''',

"3":
'''\
3333 \
   3 \
 333 \
   3 \
3333 \
''',

"4":
'''\
4 4  \
4 4  \
4444 \
  4  \
  *  \
''',

"5":
'''\
555  \
5    \
5555 \
   5 \
5555 \
''',

"6":
'''\
 66  \
6    \
6666 \
6  6 \
 66  \
''',

"7":
'''\
7777 \
   7 \
  7  \
 7   \
 7   \
''',

"8":
'''\
 88  \
8  8 \
 88  \
8  8 \
 88  \
''',

"9":
'''\
 99  \
9  9 \
 999 \
   9 \
 99  \
''',

    }


num = input("請輸入數字 0~9:")
enlarge = int(input("請輸入放大倍數 0~9:"))

for i in range(5):
    for e in range(enlarge):
        for j in range(5):
            print(numMap[num][i*5+j]*enlarge, end="")
        print()