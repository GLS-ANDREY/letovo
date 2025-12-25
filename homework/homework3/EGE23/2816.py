def from_55_to_3(start,stop):
    if start < stop:
        return 0
    if start == 18:
        return 0
    if start == stop:
        return 1
    minus_2 = from_55_to_3(start-2,stop)
    if start%2 == 0:
        divi_2 = from_55_to_3(start/2,stop)
        proverka = 1
    else:
        minus_3 = from_55_to_3(start - 3, stop)
        proverka = 0

    if proverka == 1:
        return minus_2+divi_2
    else:
        return minus_2+minus_3

print(from_55_to_3(55,3))