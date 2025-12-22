def from_21_to_2(start,stop):
    if start < stop:
        return 0
    if start == stop:
        return 1
    minus2 = from_21_to_2(start-2,stop)
    minus5 = from_21_to_2(start-5,stop)
    return minus2+minus5


print(from_21_to_2(23,2))