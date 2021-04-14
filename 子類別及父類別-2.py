class  Parent:
    def __init__(self):
        print('I am Parent')

class Child(Parent):
    def __init__(self,name):
        # super().__init__()#呼叫父類
        print(name,'is Child')
John = Child('John')#子類有 所以不呼叫父類