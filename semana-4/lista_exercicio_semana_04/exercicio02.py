
# Exercício 2
# Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

# Exemplo:
# Digite o valor de n: 5
# 1
# 3
# 5
# 7
# 9

numeroIteracoes = int(input("Digite o valor de n: "))
contador = 1

while (numeroIteracoes != 0):
    resultadoResto = contador % 2
    if (resultadoResto != 0):
        print (contador)
        numeroIteracoes = numeroIteracoes - 1
        
    contador = contador + 1

