from string import digits, ascii_uppercase

stroka = digits + ascii_uppercase
stroka = stroka[:17]
for x in stroka:
    a = "9759" + x
    b = "3" + x + "108"
    if (int(a,17) + int(b,17)) % 11 == 0:
        print((int(a,17) + int(b,17)) / 11)
