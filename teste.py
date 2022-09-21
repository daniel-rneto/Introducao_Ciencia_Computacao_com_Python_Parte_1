def ePrimo(x):
    maior_primo = 0
    contador = 0
    while (contador < x):
        
        if (contador % 2 != 0):
            maior_primo = contador
            #print (contador, " Nâo é Primo")
        contador = contador + 1

    return maior_primo

y = int(input("digite um número: "))
print ("maior primo:", ePrimo (y))