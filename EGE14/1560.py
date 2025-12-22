def to_3(n10):
    res = []
    while n10 != 0:
        ost = n10%3
        n10 = n10//3
        res = [ost] + res
    return res
print(to_3(9**11 * 3**20 - 3**9 - 27).count(2))

