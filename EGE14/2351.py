def to_27(n10):
    res = []
    while n10 != 0:
        ost = n10%27
        n10 = n10//27
        res = [ost] + res
    return res
print(to_27(2 * 729**75 + 2 * 243**78 + 81**81 + 2 * 27**84 + 2 * 9**87 + 58).count(0))