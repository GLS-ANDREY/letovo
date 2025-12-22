number_stairs = int(input("Введите номер лестницы, которую нужно построить:"))
if number_stairs >= 5 or number_stairs <= 0:
    print("Такого номера нет!")
    exit()

width_stairs = int(input("Введите ширину лестницы, которую нужно построить:"))
if width_stairs > 15:
    print("Слишком много!")
    exit()
if width_stairs < 3:
    print("Слишком мало!")
    exit()


def one(shirina):
    if shirina == 0:
        return
    one(shirina - 1)
    print("0" * shirina)


if number_stairs == 1:
    one(width_stairs)


def two(shirina):
    if shirina == 0:
        return
    print("0" * shirina)
    two(shirina - 1)


if number_stairs == 2:
    two(width_stairs)


def three(shirina, start=0):
    if start == shirina + 1:
        return
    print(" " * start, "0" * (shirina - start), sep="")
    three(shirina, start + 1)


if number_stairs == 3:
    three(width_stairs)


def four(space, shirina=1):
    if space == 0:
        return
    print(" " * (space - 1), "0" * shirina, sep="")
    four(space - 1, shirina + 1)


if number_stairs == 4:
    four(width_stairs)
