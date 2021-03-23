# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:14:11 2021

@author: user
"""

data = [ 10,20,30,40,50]

data2 = []
for i in data:
    data2.append(i)
    
data.append('A')    

print(data)
print(data2)

import copy

number = [1,2,3,4,5]
newnum = copy.copy(number)

number[0] = 99
print(newnum)

number = [1,2,3,4,5]
newnum = copy.deepcopy(number)

number[0] = 99
print(newnum)

print('-'*30)

a = [100, ['A', 'B']]
a_equal = a
b = copy.copy(a)
c = copy.deepcopy(a)
a[0] = 199    
a[1][0] = 'orange'     
print(a,id(a))
print(b,id(b))
print(c,id(c))
