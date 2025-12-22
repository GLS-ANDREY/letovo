def to_11(n10):
    res = []
    while n10 != 0:
        ost = n10%11
        n10 = n10//11
        res = [ost] + res
    return res

for x in range(0,3001):
    if to_11(9 * 11**210 + 8 * 11**150 - x).count(0) == 60:
        print(x)
