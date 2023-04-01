masculino = 'M'
feminino = 'F'
sexo = masculino and feminino

while sexo == 'M' or sexo == 'F':
    nome = str(input('Digite seu nome:'))
    sexo = str(input('Digite seu sexo:'))
    if sexo == 'F' or sexo == 'M':
        print('Você é do sexo {}' .format(sexo))
    elif sexo != masculino or feminino:
        print('Digitou algo errado!')
