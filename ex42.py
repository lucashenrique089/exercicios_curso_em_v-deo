import math
from time import sleep
print('-=-' * 15)
print('PROCESSANDO OS TRIÂNGULOS')
sleep(1.5)

r1 = float(input('Digite um valor:'))
r2 = float(input('Digite o segundo valor:'))
r3 = float(input('Digite o terceiro valor:'))

if r1 < r3 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima se formam em um triângulo')
    if r1 == r2 == r3:
        print('Esse triângulo é um EQUILÁTERO')
    if r1 != r2 != r3 != r1:
        print('Esse triângulo é um ESCALENO')
    else:
        print('Esse triângulo é um ISÓSCELES')
else:
    print('Não consigo Formar...')
