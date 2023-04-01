total = 0
maiorMil= 0
menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('Qual nome do produto:'))
    preço = float(input('Qual o preço do produto:R$'))
    cont += 1
    total += preço
    if preço > 1000:
        maiorMil += 1
    if cont == 1 or preço < menor:
        menor = preço
        produto = barato
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 20)
print(f'O total das compras ficou R$ {total}')
print(f' Temos a qauntidade de produtos acima de R$1000 de {maiorMil} ')
print(f'E o menor preço é de {menor}')
print('FIM DA ANALISE DE PRODUTOS')

