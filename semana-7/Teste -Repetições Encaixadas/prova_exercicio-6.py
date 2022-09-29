# Observe o programa abaixo:
# O que precisamos colocar na linha 5 para que o programa imprima "1 2 3 4 5 6 7 8 9"?

i = 0
while i < 3:
  j = 0
  while j < 3:
    #expressão
    print(3 * i + j + 1, end=" ")
    j = j + 1
  i = i + 1