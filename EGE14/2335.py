def to_25(n10):
    res = []
    while n10 != 0:
        ost = n10%25
        n10 = n10//25
        res = [ost] + res
    return res

print(to_25(3 * 625**173 + 4 * 125**180 + 3 * 25**157 * 2 * 5**155 + 156).count(0))







