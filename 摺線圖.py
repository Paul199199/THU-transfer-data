# -*- coding: utf-8 -*-
"""
摺線圖
"""
import matplotlib.pyplot as plt

data1 = [1,2,3,4,5,6,7,8]
data2 = [30,70,20,10,7,10,30,60]
data3 = [2,7,9,8,14,17,6,20]
data4 = [10,20,30,15,25,10,17,26]
seq = [1,2,3,4,5,6,7,8]#x軸數量線
plt.plot(seq,data1,'g--',
         seq,data2,'r-.',
         seq,data3,'y:',
         seq,data4,'k.')
plt.title('Chart',fontsize = 30)#標題大小
plt.xlabel('Value',fontsize = 18)
plt.ylabel('y_value',fontsize = 18)