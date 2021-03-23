
def personal(school='聯成',city='台中市'):#預設參數PS: name只許再參數之前不許在參數之後
    print('學校:',school)
    print('城市:',city)
personal()#------------------------------位置參數
personal('逢甲','台北市')
personal('中興')
personal(city='台南市')#------------------關鍵字函式
##PS 關鍵字之後 不許是位置