print('>' * 10, 'GERADOR DE P.A', '<' *10)
n = int(input('Dogote um valor:'))
razão = int(input('Digite o valor da razão:'))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} ► ' .format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais?'))
print('FIIM!!!')
