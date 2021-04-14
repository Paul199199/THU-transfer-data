import math
from CustomException import MyError
class Circle:
    def __init__(self,r):
        self.setR(r)
    def getR(self):
        return self.__r
    def setR(self,r):#周長
        if r > 0:
            self.__r = r
        else:
            raise MyError(r)
    def perm(self):
        return 2 * self.__r * math.pi
    
    def area(self):#面積
        return self.__r * self.__r * math.pi
    def __str__(self):
        return'圓周長:{:4.3f},圓面積:{:4.3f}'.format(self.perm(),self.area())
    
try:
    one = Circle(12)
    print(one)
    two = Circle(-12)
    print(two)
except MyError as ex:
    print(ex)