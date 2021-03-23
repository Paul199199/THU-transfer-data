# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:55:35 2021

@author: user
"""

data = {1:'Apple',20:'Banana'}
data2 = {'a':100,'b':'Banana'}
data3 = dict(a='Apple',b=300)

print(data[1])
print(data2['a'])
print(data3['a'])
print(data3['b'])

bike = {"Id":3,"StationName":"保安轉運站","Address":"保安轉運站公車侯車亭旁 (文賢路一段)","EnglishStationName":"Bao'an Bus Station","EnglishAddress":"Besides the shelter of Bao’an Bus Station (on Wenxian Rd. Section 1)","Capacity":32,"AvaliableBikeCount":21,"AvaliableSpaceCount":11,"UpdateTime":"2021-03-18T20:00:24.613","Latitude":22.932706,"Longitude":120.230637,"District":"仁德區"}

print(bike['StationName'])
print(bike['AvaliableBikeCount'])

student = {"John":90,'May':88,'Peter':93}

print(student['May'])

student['May'] = 100

print(student)

student['Sue'] = 10

print(student)


print(student.get('John'))
print(student.get('Cherry'))
print(student.get('Cherry',60))
print(student.get('John',40))














