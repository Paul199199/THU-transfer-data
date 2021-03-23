##串列生成式
# d = []
# for i in range(10):
#     d.append(i)
# print(d)
# print([x for x in range(10)])
# print()#斷行

# r = []
# for i in range(1,11):
#     if i %2 == 0:
#         r.append(i)
# print(r)
# print([i for i in range(1,11) if i%2==0])

# print()#斷行

# score = [100,60,30,59,70,41,80]
# h = [x for x in score if x >=60]
# print(len(h),'人，及格為 : ',h)


#字典判斷
score = {'tom':90,'david':70,'peter':30,'John':59,'mary':81,'may':93,'sue':60}
# print('大於70分有:',{k:v for k,v in score.items() if v>70})
# print('小於60分有:',{k:v for k,v in score.items() if v<60})

# print()#斷行

data = {}
for k,v in score.items():
    s = v//10
    if s not in data :
        data[s] = []
    data[s].append(k)
print(data)

# print()#斷行

for key in data.items():
    if isinstance(key,list):
        for value in key:
            print(value)
    else:
        print(key)

for key,v in data.items():
    if isinstance(v,list):
        for value in v:
            print(value)
    else:
        print(key)

print()#斷行        

