def from_69_to_14(start,stop,spisok):
    spisok.append(start)
    if start < stop:
        return 0
    if spisok.count(26) >= 1 and spisok.count(30) >= 1:
        return 0
    if start == stop:
        return 1

    spisok1 = spisok.copy()
    minus_3 = from_69_to_14(start-3,stop,spisok1)


    spisok2 = spisok.copy()
    divi_2 = from_69_to_14(start//2,stop,spisok2)

    return minus_3+divi_2

print(from_69_to_14(69,14,[]))


