import os
dir = 'C:\\mypython'
if os.path.exists(dir):
    print('已存在')
else:
    os.mkdir(dir)