# Exercício 1 - Removendo elementos repetidos
# Escreva a função remove_repetidos que recebe como parâmetro 
# uma lista com números inteiros, verifica se tal lista possui 
# elementos repetidos e os remove. A função deve devolver uma lista 
# correspondente à primeira lista, sem elementos repetidos. 
# A lista devolvida deve estar ordenada.

# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

# Exemplo: 
# >>>lista = [2, 4, 2, 2, 3, 3, 1]
# >>>remove_repetidos(lista)
# [1, 2, 3, 4]
# >>>remove_repetidos([1, 2, 3, 3, 3, 4])
# [1, 2, 3, 4]

def remove_repetidos(lista):
    lista.sort()
    contadorExterno = 0
    while (contadorExterno < len(lista)):
        contadorInterno = contadorExterno
        while (contadorInterno < len(lista)):
            if (contadorInterno != contadorExterno):
                if (lista[contadorExterno] == lista[contadorInterno]):
                    del lista[contadorInterno:(contadorInterno + 1)]
                    contadorInterno = contadorInterno - 1
            contadorInterno = contadorInterno + 1
        
        contadorExterno = contadorExterno + 1
        #contadorInterno = contadorExterno

    return lista


lista = [3,2,4,5,7,8,5,3,1,5,7,8,9]

#print (lista)

#print (remove_repetidos(lista))

print (remove_repetidos(lista))