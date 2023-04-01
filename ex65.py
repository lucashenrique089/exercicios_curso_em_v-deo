resposta = 'S'
soma = quantidade = média = maior = menor = 0

while resposta in 'Ss':
    n1 = int(input('Digite seu valor: '))
    soma += n1
    quantidade += 1
    if quantidade == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
média = soma / quantidade
print('A soma entre os números deu {} e a média é {}' .format(soma, média))
print('O maior valor foi {} e o menor valor foi {}' .format(maior, menor))
print('FIM')
