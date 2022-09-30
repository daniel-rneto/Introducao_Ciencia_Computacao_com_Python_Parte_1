# Exercício 2
# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
# de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

# Por exemplo:
# digite a largura: 10
# digite a altura: 3
# ##########
# #        #
# ##########

# digite a largura: 2
# digite a altura: 2
# ##
# ##

def imprime_quadrado (x,y):
    imprime_linha = 1
    imprime_coluna = 1

    while (imprime_linha <= y):
        if ((imprime_linha == 1) or (imprime_linha == y)):
            while (imprime_coluna <= x):
                print ("#", end="")
                imprime_coluna = imprime_coluna + 1
        else:
            while (imprime_coluna <= x):
                if ((imprime_coluna == 1) or (imprime_coluna == x)):
                    print ("#", end="")
                else:
                    print (" ", end="")
                imprime_coluna = imprime_coluna + 1
        print ()
        imprime_linha = imprime_linha + 1
        imprime_coluna = 1

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

imprime_quadrado(largura,altura)


