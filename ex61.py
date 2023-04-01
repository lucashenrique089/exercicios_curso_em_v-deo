n = int(input('Digite um valor:'))
razao = int(input('Digite a razão:'))
termo = n
cont = 1

while cont <= 10:
    print('{} - ' .format(termo), end='')
    termo += razao
    cont += 1
print('FIIM')

