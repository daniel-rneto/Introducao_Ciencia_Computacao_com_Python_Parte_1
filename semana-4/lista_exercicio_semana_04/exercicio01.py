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