import math

x1 = int(input("Digite a coordenada x1: "))
y1 = int(input("Digite a coordenada y1: "))
x2 = int(input("Digite a coordenada x2: "))
y2 = int(input("Digite a coordenada y2: "))

distancia = math.sqrt(((x1 + x2) ** 2) + ((y1 + y2) ** 2))

if (distancia >= 10):
    print("Longe")
else:
    print("Perto")