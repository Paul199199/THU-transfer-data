data = [62,31,90]
def demo(data):
    total = 0
    for item in data:
        assert item > 0,'輸入質為 0'#我斷言他一定大於0 否則輸入值必為0
        total += item
    return total
print('Total: ',demo(data))