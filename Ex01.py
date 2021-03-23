# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:42:32 2021

@author: user
"""

a = 100
b = a

data = [1,2,3]
data2 = data

print(id(a))
print(id(b))
print(id(data))
print(id(data2))
a = 9

data.append(100)

print()
print(id(a))
print(id(b))
print(id(data))
print(id(data2))

print(data)
print(data2)