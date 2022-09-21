# Exercício 2 - Desafio do vídeo "Repetição com while"
# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

# Exemplos:

# Digite um número inteiro: 12345
# não

# Digite um número inteiro: 1011
# sim

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
   
  
    anterior = atual

if (resp):
    print ("Sim")
else:
    print ("Não")
