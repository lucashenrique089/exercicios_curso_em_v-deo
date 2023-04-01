from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor a ser jogado:'))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Qual você quer escolher [Par/Ímpar]:')).strip().upper()[0]

    print(f'O Jogador jogou {jogador} e o computador {comp}, o total foi {total}, ', end='')
    print(' DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('PARABÉNS JOGADOR VOCÊ VENCEU')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('PARABÉNS JOGADOR VOCÊ VENCEU')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('VAMOS JOGAR NOVAMENTE???')
print(f' Parabéns você venceu {v} vezes.')


