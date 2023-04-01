from datetime import date
nome = str(input('Digite o nome do nadador:'))
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento do nadador:'))
ano_taxas = atual - nascimento
print('O atleta {} tem a idade {}' .format(nome, ano_taxas))

if ano_taxas < 9:
    print('Atleta {} Mirim.' .format(nome))
elif ano_taxas > 9 and ano_taxas < 14:
    print('O atleta {} é Infantil.' .format(nome))
elif ano_taxas > 14 and ano_taxas < 19:
    print('O Atleta {} é Junior.' .format(nome))
elif ano_taxas > 19 and ano_taxas < 25:
    print('Atleta {} é sênior.' .format(nome))
elif ano_taxas >= 25:
    print('Atleta {} MASTER' .format(nome))
else:
    print('ATLETA {} SUPREMO')
