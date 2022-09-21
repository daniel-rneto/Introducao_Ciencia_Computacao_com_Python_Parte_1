# Exercício 3
# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

# Exemplo:
# Digite um número inteiro: 123
# 6

# Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, 
# ou seja, aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira 
# jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.

numero = int(input("Digite o valor de n: "))
soma = 0

while (numero != 0):

    soma = soma + (numero % 10)
    numero = numero // 10

print (soma)