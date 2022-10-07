# Exercício 2 - Máximo com 3 parâmetros
# Reescreva a função 'maximo' do outro exercício, 
# que devolve o maior valor dentre dois inteiros recebidos, 
# para que ela passe a receber 3 valores inteiros como 
# parâmetros e devolva o maior dentre eles.

# Exemplos de execução no Python Shell
# >>>maximo(30, 14, 10)
# 30
# >>>maximo(0, -1, 1)
# 1

def maximo (a, b, c):
    if (a > b and b > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c

print (maximo(30, 14, 10))
print (maximo(0, -1, 1))