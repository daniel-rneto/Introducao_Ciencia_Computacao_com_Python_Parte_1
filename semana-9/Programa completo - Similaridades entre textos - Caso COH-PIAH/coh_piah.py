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
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade 
    nas assinaturas.'''
    cont = 0
    soma = 0

    while (cont < 6):
        soma = soma + abs(as_a[cont] - as_b[cont])
        #print ("abs(",as_a[cont],"-",as_b[cont],")")
        cont = cont + 1
    return (soma / cont)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal_a = calc_tam_medio_palavra (texto)
    ttr_a = calc_relacao_type_token (texto)
    hlr_a = calc_razao_hapax_legomana (texto)
    sal_a = tamanho_medio_sentenca (texto)
    sac_b = calc_complexidade_sentenca (texto)
    pal_a = calc_tamanho_medio_frase (texto)
    
    return [wal_a, ttr_a, hlr_a, sal_a, sac_b, pal_a]
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver 
    o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    resultados = []
    pos = 1
    for texto in textos:
        as_a = calcula_assinatura(texto)
        resultados.append(compara_assinatura(as_a, ass_cp))
    
    menor_valor = resultados[0]
    contador = 1
    while contador < len(resultados):
        if (resultados[contador] < menor_valor):
            menor_valor = resultados[contador]
            pos = contador + 1
        contador = contador + 1
    
    return pos

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##
  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  

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

def calc_tam_medio_palavra (texto):
    # Função recebe um texto e retorna o calculo do tamanho médio de palavras
    return (calc_qtde_letras_texto (texto) / calc_qtde_palavras_texto (texto))

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##

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

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##

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

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##

def calc_numero_sentencas (texto):
    # A função recebe o texto e retorna quantas sentenças tem no texto
    return len(separa_sentencas(texto))

def calc_total_caracteres_todas_sentencas (texto):
    # A função recebe um texto na entrada e devove o total de caracteres em todas as sentenças.
    total_cacteres = 0
    
    for sentencas_separadas in separa_sentencas(texto):
        total_cacteres = total_cacteres + len(sentencas_separadas)

    return total_cacteres

def tamanho_medio_sentenca (texto):
    # A função recebe um texto como parâmetro e devolve o cálculo do tamanho médio de sentença
    return (calc_total_caracteres_todas_sentencas (texto) / calc_numero_sentencas (texto))

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##

def calc_total_frases (texto):
    # A função recebe um texto na entrada e devolve o total de frases que o texto tem
    total_frases = 0
    for sentenca_separada in separa_sentencas(texto):
        total_frases = total_frases + len(separa_frases(sentenca_separada))
    
    return total_frases

def calc_complexidade_sentenca (texto):
    # A função receve um texto na entrada e retorna o calculo da Complexidade de sentença
    return (calc_total_frases (texto) / calc_numero_sentencas (texto))

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##

def calc_total_caracteres_frases (texto):
    # A função recebe um texto na entrada e devolve o número de caracteres em cada frase
    total_caracteres_frases = 0
    for sentenca_separada in separa_sentencas(texto):
        for frase_separada in separa_frases(sentenca_separada):
            total_caracteres_frases = total_caracteres_frases + len(frase_separada)
    
    return total_caracteres_frases
    
def calc_tamanho_medio_frase (texto):
    # A função recebe um texto na entrada e retorna o valor do tamanho médio de frase
    return (calc_total_caracteres_frases (texto) / calc_total_frases (texto))

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##

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

def testa_tamanho_medio_sentenca (texto):
    resultado = tamanho_medio_sentenca (texto)
    # [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
    if (resultado == 70.81818181818181):
        print ("Funcionou")
        print ("Tamanho médio da sentença:", resultado)

def testa_calc_complexidade_sentenca (texto):
    resultado = calc_complexidade_sentenca (texto)
    # [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
    if (resultado == 1.8181818181818181):
        print ("Funcionou")
        print ("Tamanho médio da sentença:", resultado)


def testa_calc_tamanho_medio_frase (texto):
    resultado = calc_tamanho_medio_frase (texto)
    # [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
    if (resultado == 38.5):
        print ("Funcionou")
        print ("Tamanho médio da sentença:", resultado)


texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
# O texto acima tem:
# 631 caracteres sem espaço, 790 caracteres com espaço
# 97 palavras diferentes
as_b = [4.51, 0.693, 0.55, 70.82, 1.82, 38.5]

textos = ["Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.",
        "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.",
        "Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens."]
