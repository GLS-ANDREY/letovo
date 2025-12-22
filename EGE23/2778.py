def rekursia(start,stop,step):
    if start > stop:
        return 0
    if start == stop:
        print(step)
        return 1
    a = rekursia(start+2,stop,step+"+2")
    b = rekursia(start+5,stop,step+"+5")
    return a + b


print(rekursia(1,21,"1"))