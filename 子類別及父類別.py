#子類別及父類別
class Mother:
    def display(self,pay):
        self.price = pay
        if self.price >=50000:
            self.price *=0.8
        print(' ={:,}'.format(self.price))
        
class Son(Mother):
    def display(self,pay):#複寫父類方法(重新定義)
        self.price = pay
        super().display(pay)
        if self.price >=50000:
            self.price *=0.9
        print('9折{:,}'.format(self.price))

mary = Mother()
John = Son()
print('60000打8折',end='')
mary.display(60000)
print('50000打9折',end='')
John.display(50000)#註解
