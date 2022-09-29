# Exercício Resolvido - com Repetições Encaixadas
# (Ler uma sequência de números digitados pelo usuário e,
# para cada número digitado, informar o seu fatorial)

def solucao_propria ():
    aux = 1
    numero = int(input("Digite um número inteiro ou 0 para sair: "))
    while (numero > 0):
        if (numero == 0):
            numero = 1
        else:
            while (numero != 0):
                
                aux = aux * numero
                #print (numero)
                numero = numero - 1
                #print (aux)
                
        print (aux)
        numero = int(input("Digite um número inteiro ou 0 para sair: "))

    #################################
    # Solução do professor
    #################################
    
n = int(input("Digite um número inteiro: "))
while (n >= 0):
    fatorial = 1
    while (n > 1):
        fatorial = fatorial * n
        n = n - 1

    print (fatorial)
    n = int(input("Digite um número inteiro: "))