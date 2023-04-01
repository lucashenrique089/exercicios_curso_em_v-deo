from datetime import date
nome = str(input('Digite seu nome:'))
atual = date.today().year
ano = int(input('Qual seu ano de nascimento:'))
idade = atual - ano
print('Quem nasceu em {} tem a idade de {} neste ano de {}' .format(ano, idade, atual))

if idade == 18:
    print('VOCÊ TEM QUE SE ALISTAR AGORA NO EXERCITO BRASILEIRO')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Fatam {} anos para alistar' .format(saldo))
    alistamento = atual + saldo
    print('Você deverá se alistar em {}' .format(alistamento))
elif idade > 18:
    saldo = idade - 18
    print('Você já passou de 18 anos, você deveria ter se alistado há {} anos' .format(saldo))
    alistamento = atual - saldo
    print('Você deveria ter se alistar em {}' .format(alistamento))

