class MyError(Exception):
    def __init__(self,r):
        self.r = r
    def __str__(self):
        return '錯誤半徑{}'.format(self.r)