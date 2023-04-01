#números primos
num = int(input('Digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('O número {} foi divisiel essas vezes {}{}' .format(num, tot, '\033[1;m'))
if tot == 2:
    print('E por isso é um número PRIMO')
else:
    print('Não é um número PRIMO')