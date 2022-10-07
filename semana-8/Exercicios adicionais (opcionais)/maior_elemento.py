﻿# Exercício 1 - Maior elemento de uma lista
# Escreva a função maior_elemento que recebe como parâmetro uma 
# lista com números inteiros e devolve um número inteiro correspondente 
# ao maior valor presente na lista recebida.

def main():

    lista = [3,2,4,5,7,88,5,3,1,5,7,8,9]
    print (maior_elemento(lista))

def maior_elemento(lista):
    contador = 0
    maior = 0
    while (contador < len(lista)):
        if (lista[contador] > maior):
            maior = lista[contador]
        contador = contador + 1
    return maior


main()