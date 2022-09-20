numeroIteracoes = int(input("Digite o valor de n: "))
contador = 1

while (numeroIteracoes != 0):
    resultadoResto = contador % 2
    if (resultadoResto != 0):
        print (contador)
        numeroIteracoes = numeroIteracoes - 1
        
    contador = contador + 1

