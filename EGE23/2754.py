def from_to(start,stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    plus_1 = from_to(start+1,stop)
    mult_4 = from_to(start*2,stop)
    plus_3 = from_to(start+3,stop)
    return plus_1+plus_3+mult_4


a = from_to(3,10)
b = from_to(10,15)
print(a*b)