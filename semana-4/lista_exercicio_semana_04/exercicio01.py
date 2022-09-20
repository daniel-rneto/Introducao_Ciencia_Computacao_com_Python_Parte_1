
#Exercício 1
#Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.

#Exemplo:
#Digite o valor de n: 5
#120

aux = 1
numero = int(input("Digite o valor de n: "))

if (numero == 0):
    numero = 1
else:
    while (numero != 0):
        
        aux = aux * numero
        #print (numero)
        numero = numero - 1
        #print (aux)
        
print (aux)