nome = str(input('Digite o nome:'))
sala = str(input('Qual a sala e série do aluno:'))
n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
media = (n1 + n2) / 2

if media <= 5.0:
    print('Aluno {} da sala e série {} está {}REPROVADO{}'.format(nome, sala, '\033[1;35m', '\033[m'))
elif media > 5.1 and media < 6.9:
    print('Aluno {} da sala e série {} está em {}RECUPERAÇÃO{}'.format(nome, sala, '\033[1;35m', '\033[m'))
elif media >= 7.0:
    print('Aluno {} da sala e série {} está {}APROVADO{}'.format(nome, sala, '\033[1;35m', '\033[m'))

print('O aluno {} teve a média {}' .format(nome, media))
