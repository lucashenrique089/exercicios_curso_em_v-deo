tot18 = 0
toth = 0
totm = 0
while True:
    idade = int(input('Digite a idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa? [M/F]')).strip().upper()[0]
    if tot18 > 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade <= 20:
        totm += 1
    if sexo == 'M' and idade > 18:
        tot18 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break
print('ACABOU OS REGISTROS')
print(f'Total de pessoas com mais de 18 foi {tot18}')
print('Total de homens cadastrados é {}'.format(toth))
print(f'O total de mulheres com menos de 20 anos foi {totm}')
print(f'O total de homens com mais de 18 anos foi {toth}')