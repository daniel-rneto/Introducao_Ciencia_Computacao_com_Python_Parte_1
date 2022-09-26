def computador_escolhe_jogada (n, m):
    return True

def usuario_escolhe_jogada (n, m):
    return True

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
        print ()
        print ("**** Rodada 1 ****")
        print ()
        qtde_pecas = int(input("Quantas peças? "))
        limite_pecas_jogada= int(input("Limite de peças por jogada? "))
        if (((limite_pecas_jogada + 1) % qtde_pecas) == 0):
            print ("Você começa!")
            usuario_escolhe_jogada (qtde_pecas, limite_pecas_jogada)

        else:
            print ("Computador começa!")
            computador_escolhe_jogada (qtde_pecas, limite_pecas_jogada)

    else:
        print ("Escolha errada. Tente novamente.")


partida()