print('=' * 30)
print('{:^30}' .format('BANCO LOC'))
print('=' * 30)
valor = int(input('Qual o valor que deseja sacar: R$'))
total = valor
ced = 50
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'O total de {totalCed}  cédulas é de {ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totalCed = 0
            if total == 0:
                break
print('=' * 30)
print('OBRIGADO, VOLTE SEMPRE')