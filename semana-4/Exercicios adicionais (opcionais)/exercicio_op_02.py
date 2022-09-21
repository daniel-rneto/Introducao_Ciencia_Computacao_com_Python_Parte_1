numero = int(input("Digite um número inteiro: "))

atual = -1
anterior = -1
resp = False

while (numero != 0):

    atual = numero % 10
    numero = numero // 10
    if (atual == anterior):
        resp = True
        numero = 0
   
    #print ("Atual:", atual)
    #print ("Anterior:", anterior)
    #print ("numero:", numero)
    #print ("resp:",resp)
    anterior = atual

if (resp):
    print ("Sim")
else:
    print ("Não")
