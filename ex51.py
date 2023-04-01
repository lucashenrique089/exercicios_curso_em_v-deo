n = int(input('Digite um valor:'))
razao = int(input('Digite a razão'))
decimo = n + (10 - 1) * razao

for c in range(n, decimo + razao, razao):
    print('{}' .format(c), end='-')
print('ACABOU')
