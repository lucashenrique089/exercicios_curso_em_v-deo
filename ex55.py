pesomaior = 0
pesomenor = 0
for c in range (1, 6):
    peso = float(input('Digite o peso da {}º aqui:' .format(c)))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso lido foi {} e o menor peso foi {}' .format(pesomaior, pesomenor))

