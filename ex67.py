while True:
    n = int(input('Qual o valor deseja para a Tabuada:'))
    if n < 0:
        break
    print('>'*10 , 'TABUADA', '<' * 10)
    for c in range (1, 11):
        print(f'{n} X {c} = {n * c}')
print('FIIM, VOLTE SEMPRE PARA MAIS TABUADA')
