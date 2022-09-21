def ePrimo(x):
    if (x > 2):
        if (x % 2 == 0):
            print ("Nâo é Primo")
        else:
            print ("Primo")

y = int(input("digite um número: "))
ePrimo (y)