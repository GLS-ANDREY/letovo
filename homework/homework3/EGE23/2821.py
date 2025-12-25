def from_120_to_6(start,stop,spisok):
    spisok.append(start)
    if start < stop:
        return 0
    if start == 40:
        return 0
    if start == stop and spisok.count(49) >= 1:
        return 1
    spisok1 = spisok.copy()
    minus_3 = from_120_to_6(start-3,stop,spisok1)
    spisok2 = spisok.copy()
    divi_2 = from_120_to_6(start//2,stop,spisok2)
    spisok3 = spisok.copy()
    divi_3 = from_120_to_6(start//3,stop,spisok3)
    return minus_3+divi_2+divi_3

print(from_120_to_6(120,6,[]))
