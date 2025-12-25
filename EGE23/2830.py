def from_to(start, stop,spisok):
    spisok.append(start)
    if start < stop:
        return 0
    if start == stop:
        return 1
    spisok1 = spisok.copy()
    minus_2 = from_to(start - 2, stop,spisok1)

    spisok2 = spisok.copy()
    divi_2 = from_to(start // 2, stop,spisok2)

    spisok3 = spisok.copy()
    divi_3 = from_to(start // 3, stop,spisok3)

    return minus_2+divi_2+divi_3

print(from_to(40,2,[]))



# spisok = [1,2,3]
#
# spisok1 = spisok[:]
# print(spisok1)
#
# spisok22 = []
# for spisok2 in spisok:
#     spisok22.append(spisok2)
# print(spisok22)
#
# spisok3 = [*spisok]
# print(spisok3)
#
# spisok4 = spisok.copy()
# print(spisok4)
#
# spisok5 = [] + spisok
# print(spisok5)
#
# spisok6 = [i for i in spisok]
# print(spisok6)
#
# spisok7 = list(spisok)
# print(spisok7)
