def func(a,b):
    try:
        result= a/b
        print(result)
    except Exception as err:
        print(err)
    finally:
        print('計算完畢')
        
func(100,5)
func(10,0)