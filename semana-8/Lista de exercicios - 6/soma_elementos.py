# Exercício 2 - Soma dos elementos de uma lista
# Escreva a função soma_elementos que recebe como parâmetro uma 
# lista com números inteiros e devolve um número inteiro correspondente 
# à soma dos elementos da lista recebida.

def soma_elementos(lista):
    soma = 0
    contador = 0
    while (contador < len(lista)):
        soma = soma + lista[contador]
        contador = contador + 1
    return soma

lista = [3,2,4,5,7,8,5,3,1,5,7,8,9]

#print (lista)

#print (remove_repetidos(lista))

print (soma_elementos(lista))