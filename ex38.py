# valores iguais, maiores e menores

n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))

if n1 < n2:
    print('O número {} é menor que o número {}'.format(n1, n2))
elif n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
elif n2 < n1:
    print('O número {} é menor que o número {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que o número {}'.format(n1, n2))
elif n1 == n2:
    print('O número {} é igual ao número {}'.format(n1, n2))
