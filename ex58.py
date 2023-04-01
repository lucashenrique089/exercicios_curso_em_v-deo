from random import randint
from time import sleep

computador = randint(0, 10)
print('Ola, eu sou seu computador...Estou escolhendo um número entre 0 à 10 tente acertar!!!')
print('Você consegue acertar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('fale seu palpite:'))
    palpites += 1
    if jogador == computador:
        acertou = computador
    else:
        if jogador < computador:
            sleep(1.0)
            print('Mais...TENTE MAIS UMA VEZ')
        elif jogador > computador:
            sleep(1.0)
            print('Menos... VAMOS LÁ TENTE MAIS VEZES')

print('PARABÉNS MEU AMIGO, VOCÊ ACERTOU!!! O NÚMERO É {} COM A QUANTIDADE DE PALPITES {}' .format(acertou, palpites))

