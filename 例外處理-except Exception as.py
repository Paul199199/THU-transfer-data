def display(a,b):
    try:
        total = a/b
        print(total)
    except Exception as ex:
        print(ex)
        # raise ex
    finally:
        print('Must be down')

try:

    display(15,5)
    display(15,0)
except Exception as e:
    print('Down',e)