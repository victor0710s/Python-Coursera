from math import sqrt

print("Vamos calcular a distancia no plano cartesiano!!!")
print("Digite quatro numeros:")
x1 = int(input("1º- "))
x2 = int(input("2º- "))
y1 = int(input("3º- "))
y2 = int(input("4º- "))

dist = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
if dist >= 10:
    print('Longe')
else:
    print('Perto')
