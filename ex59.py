from time import sleep
num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor:'))
opção = 0
print('-=-' * 10)
while opção != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    opção = int(input('Digite sua opção:'))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre os números {} + {} é igual {}' .format(num1, num2, soma))
    elif opção == 2:
        multiplica = num1 * num2
        print('A multiplicação entre os números {} X {} é igual {}' .format(num1, num2, multiplica))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior valor entre os números {} e {} é {}' .format(num1, num2, maior))
    elif opção == 4:
        print('Informe novos valores...')
        num1 = int(input('Digite o primeiro valor:'))
        num2 = int(input('Digite o segundo valor:'))
    elif opção == 5:
        print('FINALIZADO PODE SAIR')
    else:
        print('OOPÇÃO INVALIDA, TENTE MAIS UMA VEZ!!!')
sleep(2.0)
print('FIM DO PROGRAMA VOLTE SEMPRE!!!')


