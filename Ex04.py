# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:56:46 2021

@author: user
"""

name = "Peter"
pi = 3.1415926
money = 10000

print('姓名：%s存款：%d元，利率為：%f'%(name,money,pi))
print('%d元，利率為：%.2f'%(money,pi))
print('存款%10d元，利率為：%10.2f'%(money,pi))

print('存款：{:,},利率：{:.2f}'.format(money,pi))
print('存款：{0:10d}，補0：{0:0<10d}'.format(money))
print('姓名：{:>10s}君'.format(name))
print('姓名：{:<10s}君'.format(name))
print('姓名：{:^10s}君'.format(name))

