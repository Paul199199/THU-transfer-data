#無參數函數式(return none)
# def hello():
#     print('hello')
#     print('welcome')
# hello()
# hello()

# print()

# def Area(w,h):
#     area = w*h
#     return area
# print(Area(9,4))

# print()

#無參數函數式
def Circle(r):#算術運算式
    area = r*r*3.1415926
    perimeter = 2*r*3.1415926
    return area,perimeter
x,y=Circle(5)
a = Circle(10)
print(x,y)
print(a)