def from_2_to_20(start,stop):
    if start > stop:
        return 0
    if start == 11:
        return 0
    if start == stop:
        return 1
    plus_1 = from_2_to_20(start+1,stop)
    mult_2 = from_2_to_20(start*2,stop)
    sq = from_2_to_20(start**2,stop)
    return plus_1+mult_2+sq

print(from_2_to_20(2,20))

