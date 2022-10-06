# Exercicio
# Lê números do teclado. 
# 0 sai das perguntas e imprime a lista na ordem inversa

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

