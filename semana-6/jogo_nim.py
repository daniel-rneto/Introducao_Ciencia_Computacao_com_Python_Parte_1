def computador_escolhe_jogada (n, m):
    
    if (n == 0):
        print ("Fim do jogo! O computador ganhou!")
    else:
        if (m == 1):
            print ("O computador tirou uma peça.")
            n = n -1
        else:
            while (n > m):
                qtde_pecas_removidas = n
                print (qtde_pecas_removidas, " peçcas removidas")
                print (m % n)

                n = n - 1

    #print ("O computador tirou ", n," peças.")

    print ("Agora restam ", n," peças no tabuleiro.")


    usuario_escolhe_jogada (n, m)

def usuario_escolhe_jogada (n, m):
    #if (n > 0):
        qtde_pecas_removidas = int(input("Quantas peças você vai tirar? "))
        while ((qtde_pecas_removidas > m) or (qtde_pecas_removidas > n)):
            print ()
            print ("Oops! Jogada inválida! Tente de novo.")
            print ()
            qtde_pecas_removidas = int(input("Quantas peças você vai tirar? "))
            
        n = n - qtde_pecas_removidas
        
        if (n > 0):
            if ( qtde_pecas_removidas == 1):
                print ("Você tirou uma peça.")
            else:
                print ("Voce tirou", qtde_pecas_removidas, "peças.")
            
            if (n == 1):
                print ("Agora resta apenas uma peça no tabuleiro.")
            else:
                print ("Agora restam ", n, " peças no tabuleiro.")

            computador_escolhe_jogada (n, m)
        else:
            print ("Você tirou uma peça.")
            print ("Fim do jogo! O usuário ganhou!")
    #else:
        #print ("Fim do jogo! O computador ganhou!")


def partida ():
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print ("")
    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato 2")
    print ("")
    resposta  = int(input())

    if (resposta == 1):
        # Partida isolada
        print ("Voce escolheu partida isolada")
        qtde_pecas = int(input("Quantas peças? "))
        limite_pecas_jogada= int(input("Limite de peças por jogada? "))
        if (((limite_pecas_jogada + 1) % qtde_pecas) == 0):
            print ("Você começa!")
            usuario_escolhe_jogada (qtde_pecas, limite_pecas_jogada)

            

        else:
            print ("Computador começa!")
            computador_escolhe_jogada (qtde_pecas, limite_pecas_jogada)


    elif (resposta == 2):
        # Campeonato
        print ("Voce escolheu um campeonato!")
        
        qtde_jogadas = 3
        jogada = 1
        while (jogada <=3):
            print ()
            print ("**** Rodada", jogada," ****")
            print ()
            qtde_pecas = int(input("Quantas peças? "))
            limite_pecas_jogada= int(input("Limite de peças por jogada? "))
            if (((limite_pecas_jogada + 1) % qtde_pecas) == 0):
                print ("Você começa!")
                usuario_escolhe_jogada (qtde_pecas, limite_pecas_jogada)

            else:
                print ("Computador começa!")
                computador_escolhe_jogada (qtde_pecas, limite_pecas_jogada)
            
            jogada = jogada + 1

    else:
        print ("Escolha errada. Tente novamente.")


partida()