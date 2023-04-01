from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento:'))
    idade = ano_atual - nascimento
    print('Pessoa nasceu em {}'.format(nascimento))
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos pessoas maiores de 21 anos e são {}' .format(totmaior))
print('Ao todo tivemos pessoas menores de 21 e elas são {}' .format(totmenor))

