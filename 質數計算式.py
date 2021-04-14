def Prime(number):
    for i in range(2,number+1):
        for x in range(2,i):
            if i % x ==0:
                break
        else:
            print(i,'是質數')
Prime(999)
