class Father:
    def display(self,name):
        self.name = name
        print('Father name is',self.name)
        
class Mother:
    def display(self,name):
        self.name = name
        print('Mother name is',self.name)
        
class Child(Father,Mother):
    pass
class Son(Father):
    pass
print(Child.__name__,'類別,繼承 = 個父類')

for item in Child.__bases__:
    print(item)
    
John = Son()
John.display('Bill')
print(Son.__name__,'的父類')
print(Son.__bases__)

Son.__bases__ = (Mother,)#直入試變更方法
John.display('Mary')