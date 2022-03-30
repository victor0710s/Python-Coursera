from math import sqrt

print("""
      ---------------------------------
             FORMULA DE BHASKARA       
      ---------------------------------
    """)

print("Digite os valores de a, b e c.")
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
delta = pow(b, 2) - 4 * a * c
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    while delta >= 0:
        x1 = ((b*-1) + sqrt(delta)) // 2*a
        x2 = ((b*-1) - sqrt(delta)) // 2*a
        list = sorted([x1, x2])
        if delta > 0:
            print(f"as raízes da equação são {list[0]} e {list[1]}")
        elif delta == 0:
            print("a raiz dupla desta equação é", x2)
        break
