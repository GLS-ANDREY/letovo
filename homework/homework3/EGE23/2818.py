def from_2_to_76(start,stop,spisok):
    spisok.append(start)
    if start > stop:
        return 0
    if start == 8:
        return 0
    if start == stop and spisok.count(32) >= 1:
        return 1
    spisok1 = spisok.copy()
    plus_2 = from_2_to_76(start+2,stop,spisok1)
    spisok2 = spisok.copy()
    mult_2 = from_2_to_76(start*2,stop,spisok2)
    return plus_2+mult_2

print(from_2_to_76(2,76,[]))