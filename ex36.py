nome = str(input('Nome da pessoa:'))
valor_casa = float(input('Qual o valor a casa: R$'))
salario = float(input('Qual o salário dele? R$'))
anos = int(input('Em quantos anos ele irá pagar?'))
minimo = salario * 30 / 100
prestacao = valor_casa / (anos * 12)

if prestacao <= minimo:
    print('O empretimo do {} pode ser aprovado' .format(nome))
else:
    print('NÃO FOI APROVADO')