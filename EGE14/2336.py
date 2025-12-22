def to_4(n10):
    result = []
    while n10 != 0:
        ost = n10%4
        n10 = n10//4
        result = [ost] + result
    return result
print(to_4(16**18 * 4**10 - 4**6 - 16).count(3))