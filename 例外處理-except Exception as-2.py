def mathDemo(n1,n2):
    try:
        result = divmod(n1,n2) # n1 // n2  , n1 % n2
    except Exception as ex:
        print('Error: ',ex)
    else:
        print('Result: ',result)
    finally:
        print('Finished')

num1,num2 = eval(input('Type two number,use , espet: '))
mathDemo(num1,num2)