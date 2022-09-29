# Exercício 1
# Escreva um programa que recebe como entradas (utilize a função input) 
# dois números inteiros correspondentes à largura e à altura de um retângulo, 
# respectivamente. O programa deve imprimir, usando repetições encaixadas 
# (laços aninhados), uma cadeia de caracteres que represente o retângulo 
# informado com caracteres '#' na saída.

# Exemplo:
# digite a largura: 10
# digite a altura: 3
# ##########
# ##########
# ##########

# Dica: lembre-se que a função print pode receber um parametro 'end', que altera 
# o último caractere da cadeia, tornando possível a remoção da quebra de linha 
# (reveja as vídeo-aulas)

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

linha = 0
coluna = 0

while (linha < altura):
    while (coluna < largura):
        print ("#", end="")
        coluna = coluna + 1
    print ()
    linha = linha + 1
    coluna = 0
    