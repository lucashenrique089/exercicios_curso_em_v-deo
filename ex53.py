frase = str(input('Digite sua frase:')).strip().upper()
separar = frase.split()
junto = ''.join(separar)
inverso = ''

for letra in range(len(junto) -1, -1, -1 ):
    inverso += junto[letra]
if inverso == junto:
    print('É um PALÍNDROMO')
else:
    print('Não é um Palíndromo')

print('A frase {} pode ser lida desta duas formas {} e {}' .format(frase, junto, inverso))

