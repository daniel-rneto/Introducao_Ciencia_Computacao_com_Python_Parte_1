# Exercício 3 - Vogais
# Escreva a função vogal que recebe um único caractere como parâmetro e devolve 
# True se ele for uma vogal e False se for uma consoante.

# Exemplos de execução no shell de Python
# >>> vogal("a")
# True
# >>> vogal("b")
# False
# >>> vogal("E")
# True

def vogal(letra):
    if (letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U"):
        return True
    else:
        return False

