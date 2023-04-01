num = cont = soma = 0
num = int(input('Digite seu número aqui:'))

while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digite seu número aqui:'))
print('FIIIM')
print('Você digitou a quantidade de números de {}' .format(cont))
print('E a soma foi {}' .format(soma))

