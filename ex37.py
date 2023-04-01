n1 = int(input('Digite um número:'))
print('''Escolha uma dessas bases!!!
[1] Para BINÁRIO
[2] Para OCTAL
[3] para HEXADECIMAL''')
opcao = int(input('Digite a opção:'))

if opcao == 1:
    print('O valor de {} em BINÁRIO é {}' .format(n1, bin(n1)[2:]))
elif opcao == 2:
    print('O valor de {} em OCTAL é {}' .format(n1, oct(n1)[2:]))
elif opcao == 3:
    print('O valor de {} em HEXADECIMAL é {}' .format(n1, hex(n1)[2:]))
else:
    print('Nenhum valor digitado...')
