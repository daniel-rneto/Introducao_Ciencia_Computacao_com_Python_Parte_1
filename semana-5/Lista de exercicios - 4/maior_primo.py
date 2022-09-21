# Exercício 2 - Primos
# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 
# como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

# Exemplos de execução no shell do Python:

# >>> maior_primo(100)
# 97
# >>> maior_primo(7)
# 7

def ePrimo(x):
    maior_primo = 0
    contador = 0
    while (contador < x):
        
        if (contador % 2 != 0):
            maior_primo = contador
            #print (contador, " Nâo é Primo")
        contador = contador + 1

    return maior_primo

def maior_primo(n):
    #<Código do maior_primo>
    return n


y = int(input("digite um número: "))
print ("maior primo:", ePrimo (y))