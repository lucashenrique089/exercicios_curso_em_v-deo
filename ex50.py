soma = 0
cont = 0
for num in range(1, 7):
    n = int(input('Digite um número aqui:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou números {} PARES e a soma foi {}' .format(cont, soma))


