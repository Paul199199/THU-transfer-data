#可切換右方Plots顯示結果
import matplotlib.pyplot as plt
data = [1,3,7,9,13,21]
data2 = [3,1,2,14,15,30]

plt.plot(data,linewidth=5,c = 'red')#線寬,線顏色
plt.plot(data2)
plt.axis([0,6,0,30])#從0開始,限制圖表上限

plt.show()