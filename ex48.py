#soma entre números ímpares multiplos de três

soma = 0
cont = 0

for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma += impar
        cont += 1
print('O total contado é {} e a soma total de tudo deu {}' .format(cont, soma))
