def from_1_to_21(start,stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    plus2 = from_1_to_21(start+2,stop)
    plus5 = from_1_to_21(start+5,stop)
    return plus2+plus5


print(from_1_to_21(1,20))