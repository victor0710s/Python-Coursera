# imprimir somente o digito da dezenas
num = int(input('Digite um número inteiro: '))
dz = (num // 10) % 10
print(f'O dígito das dezenas é {dz}')
