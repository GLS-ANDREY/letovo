def from_2_to_45(start,stop,spisok):
    spisok.append(start)
    if start > stop:
        return 0
    if start == stop and spisok.count(15) >= 1:
        return 1
    spisok1 = spisok.copy()
    plus_1 = from_2_to_45(start+1,stop,spisok1)

    spisok2 = spisok.copy()
    mult_2 = from_2_to_45(start*2,stop,spisok2)
    return plus_1+mult_2

print(from_2_to_45(2,45,[]))