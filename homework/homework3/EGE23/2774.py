def from_36_to_2(start, stop, spisok):
    spisok.append(start)
    if start < stop:
        return 0
    if start == stop and spisok.count(8) >= 1:
        return 1
    spisok1 = spisok.copy()
    minus_2 = from_36_to_2(start - 2, stop, spisok1)

    spisok2 = spisok.copy()
    divi_2 = from_36_to_2(start // 2, stop, spisok2)

    return minus_2+divi_2

print(from_36_to_2(36,2,[]))