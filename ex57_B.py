sexo = str(input('Digite seu Sexo [M/F]:')).strip().upper()[0]
idade = int(input('Digite sua idade:'))

while sexo not in 'MF':
    sexo = str(input('Dados Invalidos, esse é seu sexo correto?')).strip().upper()[0]
print('Sexo {} foi registado' .format(sexo))
