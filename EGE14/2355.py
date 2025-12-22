def to_7(n10):
    res = []
    while n10 !=0:
        ost = n10%7
        n10 = n10//7
        res = [ost] + res
    return res

for x in range(0,2300):
    if to_7(7**350 + 7**150 - x).count(0) == 200:
        print(x)