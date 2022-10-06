# Exercicio
# Lê números do teclado. 
# 0 sai das perguntas e imprime a lista na ordem inversa

lista_numero = []

#numero = int(input("Digite um número OU 0 para sair: "))
numero = 1
while (numero != 0):
    numero = int(input("Digite um número OU 0 para sair: "))
    if (numero != 0):
        lista_numero.append(numero)
    

print (lista_numero)
