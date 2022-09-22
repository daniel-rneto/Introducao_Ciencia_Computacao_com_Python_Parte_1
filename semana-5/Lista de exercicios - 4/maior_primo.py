# Exercício 2 - Primos
# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 
# como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

# Exemplos de execução no shell do Python:

# >>> maior_primo(100)
# 97
# >>> maior_primo(7)
# 7

def ePrimo(x):
    if ((x == 2) or (x == 3) or (x == 5) or (x == 7)):
        #print (x, "é primo")
        return True
    else:
        if ((x % 2 == 0) or (x % 3 == 0) or (x % 5 == 0) or (x % 7 == 0)):
            #print ("False")
            return False
        else:
            #print ("True")
            return True


def maior_primo(n):
    maior_primo = 0
    contador = 2
    while (contador <= n):
        
        if (ePrimo(contador)):
            #print (contador)
            maior_primo = contador
        contador = contador + 1

    return maior_primo
