def to_31(n10):
    res = []
    while n10 != 0:
        ost = n10%31
        n10 = n10//31
        res = [ost] + res
    return res



a = to_31(3 * 289**2024 + 81 * 49**121 - 9 * 16**81 - 6011)
a = [b for b in a if b < 18]
print(sum(a))