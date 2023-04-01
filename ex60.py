#calculos fatoriais
# exemplo 5! = 5x4x3x2x1 = 120
#from math import factorial
#f = factorial(n)
#print('O fatorial de {} é {}' .format(n,f))

n = int(input('Digite um valor:'))
c = n
f = 1
print('CALCULO FATORIAL')
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f=f*c
    c -= 1
print(' O fatorial é {}' .format(f))




