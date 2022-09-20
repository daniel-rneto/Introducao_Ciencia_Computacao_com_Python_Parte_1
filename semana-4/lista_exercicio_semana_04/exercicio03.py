numero = int(input("Digite o valor de n: "))
soma = 0

while (numero != 0):

    soma = soma + (numero % 10)
    numero = numero // 10

print (soma)