def pir(n1,n2):
    if n2 == 0:
        exit()
    print(" "*n1,"0"*n2,sep="")
    return pir(10-(n2-2),n2-2)

print(pir(0,10))

