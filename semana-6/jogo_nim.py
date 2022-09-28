def computador_escolhe_jogada (n, m):
    jogada = 1
    
    while (jogada <= m):
        if ((n-jogada) % (m + 1) == 0):
            #print ("Entrou")
            return jogada
        else:
            return m
        
def usuario_escolhe_jogada (n, m):

    qtde_pecas_removidas = int(input("Quantas peças você vai tirar? "))
    while ((qtde_pecas_removidas > m) or (qtde_pecas_removidas > n) or (qtde_pecas_removidas <= 0)):
        print ()
        print ("Oops! Jogada inválida! Tente de novo.\n")
        # print ()
        qtde_pecas_removidas = int(input("Quantas peças você vai tirar? "))
        
    return qtde_pecas_removidas

def partida ():
    
    qtde_pecas = int(input("Quantas peças? "))
    limite_pecas_jogada= int(input("Limite de peças por jogada? "))
    if (((limite_pecas_jogada + 1) % qtde_pecas) == 0):
        print ("Você começa!")
        
        # True = usuário joga / False = computador joga
        jogada = True

        while (qtde_pecas > 0):
            if (jogada):
                jogada = False
                pecas_removidas = usuario_escolhe_jogada (qtde_pecas, limite_pecas_jogada)
                qtde_pecas = qtde_pecas - pecas_removidas

                if ( pecas_removidas == 1):
                    print ("Você tirou uma peça.\n")
                else:
                    print ("Voce tirou", pecas_removidas, "peças.\n")

                if (qtde_pecas == 1):
                    print ("Agora resta apenas uma peça no tabuleiro.\n")
                elif (qtde_pecas == 0):
                    print ("Fim do jogo! O computador ganhou!")
                else:
                    print ("Agora restam", qtde_pecas, "peças no tabuleiro.\n")
            else:
                jogada = True
                pecas_removidas = computador_escolhe_jogada (qtde_pecas, limite_pecas_jogada)
                qtde_pecas = qtde_pecas - pecas_removidas

                if ( pecas_removidas == 1):
                    print ("O computador tirou uma peça.\n")
                else:
                    print ("O computador tirou", pecas_removidas, "peças.\n")
                
                if (qtde_pecas == 1):
                    print ("Agora resta apenas uma peça no tabuleiro.\n")
                elif (qtde_pecas == 0):
                    print ("Fim do jogo! O computador ganhou!")
                else:
                    print ("Agora restam", qtde_pecas, "peças no tabuleiro.\n")
                

    else:
        print ("Computador começa!")

        # True = usuário joga / False = computador joga
        jogada = False

        while (qtde_pecas > 0):
            if (jogada):
                jogada = False
                pecas_removidas = usuario_escolhe_jogada (qtde_pecas, limite_pecas_jogada)
                qtde_pecas = qtde_pecas - pecas_removidas

                if ( pecas_removidas == 1):
                    print ("Você tirou uma peça.\n")
                else:
                    print ("Você tirou", pecas_removidas, "peças.\n")

                if (qtde_pecas == 1):
                    print ("Agora resta apenas uma peça no tabuleiro.\n")
                elif (qtde_pecas == 0):
                    print ("Fim do jogo! O computador ganhou!")
                else:
                    print ("Agora restam", qtde_pecas, "peças no tabuleiro.\n")
            else:
                jogada = True
                pecas_removidas = computador_escolhe_jogada (qtde_pecas, limite_pecas_jogada)
                qtde_pecas = qtde_pecas - pecas_removidas

                if ( pecas_removidas == 1):
                    print ("O computador tirou uma peça.\n")
                else:
                    print ("O computador tirou", pecas_removidas, "peças.\n")
                
                if (qtde_pecas == 1):
                    print ("Agora resta apenas uma peça no tabuleiro.\n")
                elif (qtde_pecas == 0):
                    print ("Fim do jogo! O computador ganhou!")
                else:
                    print ("Agora restam", qtde_pecas, "peças no tabuleiro.\n")
                

def main ():
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print ("")
    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato 2")
    print ("")
    resposta  = int(input())

    if (resposta == 1):
        # Partida isolada
        print ("Voce escolheu partida isolada")
        partida()
    elif (resposta == 2):
        # Campeonato
        print ("Voce escolheu um campeonato!")
    else:
        print ("Escolha errada. Tente novamente.")

main()