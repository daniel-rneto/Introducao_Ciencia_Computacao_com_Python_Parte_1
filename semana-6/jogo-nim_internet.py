def computador_escolhe_jogada(n,m):
    if (m + 1) >= n:
        Peças_retiradas_pelo_computador = n
    else:
        Peças_retiradas_pelo_computador = n - (m+1)
    Peças_restantes_no_tabuleiro = n - Peças_retiradas_pelo_computador
    if Peças_retiradas_pelo_computador != 1:
        print ("O computador tirou",Peças_retiradas_pelo_computador, "peças ")
    else:
        print ("O computador tirou uma peça ")
    if Peças_restantes_no_tabuleiro != 1:
        print("Agora restam", Peças_restantes_no_tabuleiro, "peças no tabuleiro.")
    else:
        print("Agora resta uma peça no tabuleiro. ")
    return Peças_restantes_no_tabuleiro

def usuario_escolhe_jogada (n,m):
    Peças_retiradas_pelo_usuario = int(input("Quantas peças você vai tirar?"))
    temp = 0
    while temp != 1:
        print("Oops! Jogada inválida! Tente de novo.")
        Peças_retiradas_pelo_usuario = int(input("Quantas peças você vai tirar?"))
        if (Peças_retiradas_pelo_usuario < n):
            temp = 1
        elif (Peças_retiradas_pelo_usuario < m) :
            temp = 1
        else:
            temp = 0
    Peças_restantes_no_tabuleiro = n - Peças_retiradas_pelo_usuario
    if Peças_retiradas_pelo_usuario != 1:
        print("você tirou", Peças_retiradas_pelo_usuario, " peças ")
    else:
        print("Voçê tirou uma peça ")
    if Peças_restantes_no_tabuleiro != 1:
        print("Agora restam", Peças_restantes_no_tabuleiro, "peças no tabuleiro.")
    else:
        print("Agora resta uma peça no tabuleiro. ")
    return Peças_restantes_no_tabuleiro

def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    x = 0
    y = 0
    z = 0
    Peças_restantes_no_tabuleiro_na_vez_do_usuario = n
    Peças_restantes_no_tabuleiro_na_vez_da_maquina = n
    if n == m:
        temp = 0
        print("Computador começa!")
        while temp != 1:
            Peças_restantes_no_tabuleiro_na_vez_da_maquina = computador_escolhe_jogada(n, m)
            n = Peças_restantes_no_tabuleiro_na_vez_da_maquina
            if n != 0:
                Peças_restantes_no_tabuleiro_na_vez_do_usuario = usuario_escolhe_jogada(n, m)
                n = Peças_restantes_no_tabuleiro_na_vez_do_usuario
            else:
                Peças_restantes_no_tabuleiro_na_vez_do_usuario = n
            n = Peças_restantes_no_tabuleiro_na_vez_do_usuario
            if (0 != Peças_restantes_no_tabuleiro_na_vez_do_usuario):
                temp = 0
            elif (Peças_restantes_no_tabuleiro_na_vez_da_maquina != 0):
                temp = 0
            else:
                temp = 1
        if Peças_restantes_no_tabuleiro_na_vez_da_maquina != 0:
            y = 1
        else:
            y = 2
        if Peças_restantes_no_tabuleiro_na_vez_do_usuario != 0:
            x = 1
        else:
            x = 2
        if (y == 2):
            print("Fim do jogo! O computador ganhou!")
            z = -1
            return z
        elif (x == 2) and (x != 2):
            print("Fim do jogo! Você ganhou!")
            w = 1
            return w
        else:
            print("")
    elif (m + 1) % n == 0:
        print("Voçê começa!")
        temp = 0
        while temp != 1:
            Peças_restantes_no_tabuleiro_na_vez_do_usuario = usuario_escolhe_jogada(n, m)
            n = Peças_restantes_no_tabuleiro_na_vez_do_usuario
            if n != 0:
                Peças_restantes_no_tabuleiro_na_vez_da_maquina = computador_escolhe_jogada(n, m)
                n = Peças_restantes_no_tabuleiro_na_vez_do_usuario
            else:
                Peças_restantes_no_tabuleiro_na_vez_da_maquina = 0
            if (0 != Peças_restantes_no_tabuleiro_na_vez_do_usuario):
                temp = 0
            elif (Peças_restantes_no_tabuleiro_na_vez_da_maquina != 0):
                temp = 0
            else:
                temp = 1
        if Peças_restantes_no_tabuleiro_na_vez_do_usuario != 0:
            x = 1
        else:
            x = 2
        if Peças_restantes_no_tabuleiro_na_vez_da_maquina != 0:
            y = 1
        else:
            y = 2
        if (x == 2):
            print("Fim do jogo! Você ganhou!")
            w = 1
            return w
        elif (y == 2) and (x != 2):
            print("Fim do jogo! O computador ganhou!")
            z = -1
            return z
        else:
            print("")
    elif (n % (m + 1) == 0):
        print("Voçê começa!")
        temp = 0
        while temp != 1:
            Peças_restantes_no_tabuleiro_na_vez_do_usuario = usuario_escolhe_jogada(n, m)
            n = Peças_restantes_no_tabuleiro_na_vez_do_usuario
            if n != 0:
                Peças_restantes_no_tabuleiro_na_vez_da_maquina = computador_escolhe_jogada(n, m)
                n = Peças_restantes_no_tabuleiro_na_vez_do_usuario
            else:
                Peças_restantes_no_tabuleiro_na_vez_da_maquina = 0
            if (0 != Peças_restantes_no_tabuleiro_na_vez_do_usuario):
                temp = 0
            elif (Peças_restantes_no_tabuleiro_na_vez_da_maquina != 0):
                temp = 0
            else:
                temp = 1
        if Peças_restantes_no_tabuleiro_na_vez_do_usuario != 0:
            x = 1
        else:
            x = 2
        if Peças_restantes_no_tabuleiro_na_vez_da_maquina != 0:
            y = 1
        else:
            y = 2
        if (x == 2):
            print("Fim do jogo! Você ganhou!")
            w = 1
            return w
        elif (y == 2) and (x != 2):
            print("Fim do jogo! O computador ganhou!")
            z = -1
            return z
        else:
            print("")
    else:
        temp = 0
        print("Computador começa!")
        while temp != 1:
            Peças_restantes_no_tabuleiro_na_vez_da_maquina = computador_escolhe_jogada(n, m)
            n = Peças_restantes_no_tabuleiro_na_vez_da_maquina
            if n != 0:
                Peças_restantes_no_tabuleiro_na_vez_do_usuario = usuario_escolhe_jogada(n, m)
                n = Peças_restantes_no_tabuleiro_na_vez_do_usuario
            else:
                Peças_restantes_no_tabuleiro_na_vez_do_usuario = n
            n = Peças_restantes_no_tabuleiro_na_vez_do_usuario
            if (0 != Peças_restantes_no_tabuleiro_na_vez_do_usuario):
                temp = 0
            elif (Peças_restantes_no_tabuleiro_na_vez_da_maquina != 0):
                temp = 0
            else:
                temp = 1
        if Peças_restantes_no_tabuleiro_na_vez_da_maquina != 0:
            y = 1
        else:
            y = 2
        if Peças_restantes_no_tabuleiro_na_vez_do_usuario != 0:
            x = 1
        else:
            x = 2
        if (y == 2):
            print("Fim do jogo! O computador ganhou!")
            z = -1
            return z
        elif (x == 2) and (x != 2):
            print("Fim do jogo! Você ganhou!")
            w = 1
            return w
        else:
            print("")

def campeonato ():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato ")
    escolha = int(input(""))
    temp = 0
    while temp != 1:
        if escolha == 1 :
            print("Voce escolheu uma partida isolada")
            print("")
            temp = 1
        elif escolha == 2 :
            print("Voce escolheu um campeonato!")
            print("")
            temp = 1
        else:
            print("Valor inválido. Por favor selecione novamente")
            escolha = int(input(""))
            temp = 3
    if escolha == 1:
        partida()
    else:
        Numero_de_partidas = 1
        Numero_de_vitorias_para_o_computador = 0
        Numero_de_vitorias_para_o_usuario = 0
        f = 0
        while f != 3:
            print("**** Rodada",Numero_de_partidas,"****")
            temp = partida()
            if temp < 0:
                Numero_de_vitorias_para_o_computador = Numero_de_vitorias_para_o_computador + (-1) * temp
                Numero_de_vitorias_para_o_usuario = Numero_de_vitorias_para_o_usuario
            else:
                Numero_de_vitorias_para_o_usuario = Numero_de_vitorias_para_o_usuario + temp
                Numero_de_vitorias_para_o_computador = Numero_de_vitorias_para_o_computador
            if Numero_de_vitorias_para_o_computador == 3:
                f = 3
            elif Numero_de_vitorias_para_o_usuario == 3:
                f = 3
            else:
                f = 0
            Numero_de_partidas = Numero_de_partidas + 1
        print("")
        print("**** Final do campeonato! ****")
        print("")
        print("Placar: Você", Numero_de_vitorias_para_o_usuario,"X",Numero_de_vitorias_para_o_computador, "Computador")

campeonato()