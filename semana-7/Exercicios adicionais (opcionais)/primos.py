# Exercício 1 - Primos
# Escreva a função n_primos que recebe como argumento um número
# inteiro maior ou igual a 2 como parâmetro e devolve a quantidade 
# de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

# Exemplo:
# >>>n_primos(2)
# 1
# >>>n_primos(4)
# 2
# >>>n_primos(121)
# 30

def ePrimo (x):
    fator = 2
    if (x == 2):
        return True
    
    while ((x % fator != 0) and fator <= x/2):
        fator =  fator + 1
    
    if (x % fator == 0):
        return False
    else:
        return True

def n_primos (x):
    totalNumerosPrimos = 0
    contador = 2
    while (contador <= x):
        if (ePrimo(contador)):
            totalNumerosPrimos = totalNumerosPrimos + 1
        contador = contador + 1

    return totalNumerosPrimos

print (n_primos(2))
print (n_primos(4))
print (n_primos(121))