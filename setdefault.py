##setdefault概念運用
fruits = {'apple':80,'banana':30,'orange':50}
n = fruits.setdefault('banana')
print(n)
n = fruits.setdefault('orange',150)
print(n)

n = fruits.setdefault('cherry',300)
print(n)
n = fruits.setdefault('cherry',400)
print(n)
print(fruits)