from random import randint
from time import sleep
print('{}'.format('\033[1;30;44m'), '-=-' * 10, 'JOKENPO', '-=-' * 10, '{}' .format('\033[m'))

print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
jogador = int(input('Fale sua opção: '))
print('-=-' * 10)

print('JO')
sleep(0.5)
print('KENPO')
sleep(0.5)

print('O computador jogou {}' .format(itens[computador]))
print('O jogador jogou {}' .format(itens[jogador]))
print('-=-' * 10)

if computador == 0: #PEDRA

    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR WINS')

    elif jogador == 2:
        print('COMPUTADOR WINS')

    else:
        print('Jogada Inválida!!!')

if computador == 1: # PAPEL

    if jogador == 0:
        print('COMPUTADOR WINS')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR WINS')

    else:
        print('Jogada Inválida!!!')

if computador == 2: # TESOURA

    if jogador == 0:
        print('JOGADOR WINS')

    elif jogador == 1:
        print('COMPUTADOR WINS')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('Jogada Inválida!!!')





