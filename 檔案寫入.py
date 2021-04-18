import os
newpath = os.path.join('c:\\mypython','lcc.txt')
#a = 連續性寫入
#w = 覆蓋性寫入
with open(newpath,'a',encoding='UTF-8') as fo:
     fo.write('連成電腦\n')

