def from_3_to_49(start, stop):
    if start > stop:
        return 0
    if start == 13:
        return 0
    if start == stop:
        return 1
    plus_2 = from_3_to_49(start+2,stop)
    mult_3 = from_3_to_49(start*3,stop)
    sq = from_3_to_49(start**2,stop)
    return plus_2+mult_3+sq

print(from_3_to_49(3,49))