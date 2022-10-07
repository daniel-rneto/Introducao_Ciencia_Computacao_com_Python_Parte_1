# Exercício 2 - Invertendo sequência
# Como pedido na primeira video-aula desta semana, escreva um programa 
# que recebe uma sequência de números inteiros e imprima todos os valores 
# em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) 
# não deve fazer parte da sequência.

# Exemplo:

# Digite um número: 1
# Digite um número: 7
# Digite um número: 4
# Digite um número: 0

# 4
# 7
# 1

def main ():
    lista_numero = []

    numero = 1

    while (numero != 0):
        numero = int(input("Digite um número OU 0 para sair: "))
        if (numero != 0):
            lista_numero.append(numero)

    print (inverte_lista(lista_numero))

def inverte_lista (lista):
    contador = (len(lista) - 1)
    lista_invertida = []
    while (contador >= 0):
        lista_invertida.append(lista[contador])
        contador = contador - 1
    return lista_invertida

main()
