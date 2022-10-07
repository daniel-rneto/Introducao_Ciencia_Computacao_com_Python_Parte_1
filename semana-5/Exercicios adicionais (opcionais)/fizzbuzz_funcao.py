# Exercício 1 - FizzBuzz
# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

# 'Fizz' se o número for divisível por 3 e não for divisível por 5;

# 'Buzz' se o número for divisível por 5 e não for divisível por 3;

# 'FizzBuzz' se o número for divisível por 3 e por 5;

# Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

# Exemplos de execução no Python Shell
# >>>fizzbuzz(3)
# "Fizz"
# >>>fizzbuzz(5)
# "Buzz"
# >>>fizzbuzz(15)
# "FizzBuzz"
# >>>fizzbuzz(4)
# 4

def fizzbuzz (numero):
    resposta = 0

    if ((numero % 3 == 0) and (numero % 5 == 0)):
        resposta = "FizzBuzz"
    elif ((numero % 3 == 0) and not(numero % 5 == 0)):
        resposta = "Fizz"
    elif (not(numero % 3 == 0) and (numero % 5 == 0)):
        resposta = "Buzz"
    elif (not (numero % 3 == 0) and not(numero % 5 == 0)):
        resposta = numero

    
    return resposta

def main():
    print (fizzbuzz (3))
    print (fizzbuzz (5))
    print (fizzbuzz (15))
    print (fizzbuzz(4))

main()