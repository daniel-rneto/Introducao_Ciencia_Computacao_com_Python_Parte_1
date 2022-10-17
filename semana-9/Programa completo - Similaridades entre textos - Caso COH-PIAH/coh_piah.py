import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

################################
def calc_tam_medio_palavra (texto):
    # Função recebe um texto e retorna o calculo do tamanho médio de palavras
    return (calc_qtde_letras_texto (texto) / calc_qtde_palavras_texto (texto))

def calc_qtde_letras_texto (texto):
    # Função recebe um texto e retorna quantos caracteres tem o texto. 
    # Não conta espaços em branco e pontuação como por exemplo . , : ; ! ?
    qtde_letras = 0
    for sentenca_separada in separa_sentencas(texto):
        for frase_separada in separa_frases(sentenca_separada):
            for palavra_separada in separa_palavras(frase_separada):
                qtde_letras = qtde_letras + len(palavra_separada)
    
    return qtde_letras

def calc_qtde_palavras_texto (texto):
    # Função recebe um texto e retorna quantas palavras tem o texto. 
    qtde_palavras = 0
    for sentenca_separada in separa_sentencas(texto):
        for frase_separada in separa_frases(sentenca_separada):
            qtde_palavras = qtde_palavras + len(separa_palavras(frase_separada))
    
    return qtde_palavras

def calc_qtde_palavras_diferentes_texto (texto):
    # Função recebe um texto e retorna quantas palavras diferentes o texto tem. 
    lista_palavras_texto = []
    for sentenca_separada in separa_sentencas(texto):
        for frase_separada in separa_frases(sentenca_separada):
            for palavra_separada in separa_palavras(frase_separada):
                lista_palavras_texto.append(palavra_separada)

    return n_palavras_diferentes(lista_palavras_texto)

def calc_relacao_type_token (texto):
    # A função recebe o texto e retorna o valor da relação Type Token
    return (calc_qtde_palavras_diferentes_texto (texto) / calc_qtde_palavras_texto (texto))

def calc_qtde_palavras_unicas_texto (texto):
    # Função recebe um texto e retorna quantas palavras únicas tem o texto. 
    lista_palavras_unicas_texto = []
    for sentenca_separada in separa_sentencas(texto):
        for frase_separada in separa_frases(sentenca_separada):
            for palavra_separada in separa_palavras(frase_separada):
                lista_palavras_unicas_texto.append(palavra_separada)

    return n_palavras_unicas(lista_palavras_unicas_texto)

def calc_razao_hapax_legomana (texto):
    # A função recebe um texto e retorna o valor da Razão Hapax Legomana
    return (calc_qtde_palavras_unicas_texto (texto) / calc_qtde_palavras_texto (texto))

def calc_numero_sentencas (texto):
    
    pass
#####################
#### T E S T E S ####
#####################

def testa_calc_qtde_letras_texto (texto):
    # 631 caracteres sem espaço, 790 caracteres com espaço
    # 97 palavras diferentes
    resultado = calc_qtde_letras_texto (texto)
    if ( resultado == 631):
        print ("Funcionou")
        print ("Quantidade de letras:", resultado)
    else:
        print ("ERRO")
        print ("Quantidade de letras diferente.")

def testa_qtde_palavras_texto (texto):
    # 140 palavras
    resultado = calc_qtde_palavras_texto (texto)
    if ( resultado == 140):
        print ("Funcionou")
        print ("Quantidade de palavras:", resultado)
    else:
        print ("ERRO")
        print ("Quantidade de palavras diferente.")
        print (resultado)

def testa_calc_tam_medio_palavra (texto):
    resultado = calc_tam_medio_palavra(texto)
    # [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
    if (resultado == 4.507142857142857):
        print ("Funcionou")
        print ("Tamanho médio de palavra:", resultado)

def testa_calc_qtde_palavras_diferentes_texto (texto):
    # 97 palavras diferentes
    resultado = calc_qtde_palavras_diferentes_texto (texto)
    if (resultado == 97):
        print ("Funcionou")
        print ("A quantidade de palavras diferentes:", resultado)
    else:
        print ("ERRO")
        print (resultado)

def testa_calc_relacao_type_token (texto):
    resultado = calc_relacao_type_token (texto)
    # [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
    if (resultado == 0.6928571428571428):
        print ("Funcionou")
        print ("Tamanho médio de palavra:", resultado)

def testa_calc_razao_hapax_legomana (texto):
    resultado = calc_razao_hapax_legomana (texto)
    # [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
    if (resultado == 0.55):
        print ("Funcionou")
        print ("Tamanho médio de palavra:", resultado)

texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
# O texto acima tem:
# 631 caracteres sem espaço, 790 caracteres com espaço
# 97 palavras diferentes
