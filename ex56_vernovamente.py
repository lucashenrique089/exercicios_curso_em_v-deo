somaidade = 0
mediaidade = 0
maioridade_homem = 0
nomevelho = ''
menoridade_mulher = 0
nomemaisnova=''

for pessoa in range (1, 5):
    print('---- {}ºPESSOA----' .format(pessoa))
    nome = str(input('Digite o nome:')).strip()
    idade = int(input('Digite a idade:'))
    sexo = str(input('[M/F]')).upper().strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridade_homem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nomevelho = nome
    if pessoa == 1 and sexo in 'Ff':
        menoridade_mulher = idade
        nomemaisnova = nome
    if sexo in 'Ff' and idade < 20:
        menoridade_mulher += 1


mediaidade = somaidade /4
print('A média de idade das pessoas situadas é {}' .format(mediaidade))
print('O homem mais velho se chama {} e tem a idade de {}' .format(nomevelho, maioridade_homem))
print('A mulher mais nova se chama {} e tem a idade de {}' .format(nomemaisnova, menoridade_mulher))



