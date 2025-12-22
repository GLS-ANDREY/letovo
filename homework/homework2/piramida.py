osnovanie_pir = int(input("Ширина основания пирамиды:"))
if osnovanie_pir%2 == 0:
    print("Не, чето не хочу, пока")
    exit()
if osnovanie_pir > 15:
    print("Больше 15 цифр не перевариваю")
    exit()
if osnovanie_pir <= 3:
    print("Маловато")
    exit()

def pir(nast_osnovanie,start_osnovanie):
    if 0 >= nast_osnovanie:
        return
    pir(nast_osnovanie - 2,start_osnovanie)
    print(" "*((start_osnovanie-nast_osnovanie)//2),"0" * nast_osnovanie,sep="")

pir(osnovanie_pir,osnovanie_pir)