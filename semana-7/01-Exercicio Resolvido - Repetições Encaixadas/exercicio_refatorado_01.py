# Mesmo exercício anterior, só que o calculo do fatorial fica em uma funcao a parte

def fatorial (x):
    fatorial = 1
    while (x > 1):
        fatorial = fatorial * x
        x = x - 1
    return fatorial


def main():
    n = int(input("Digite um número inteiro: "))
    while (n >= 0):
        print (fatorial (n))
        n = int(input("Digite um número inteiro: "))

main()