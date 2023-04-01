from time import sleep

print('*' * 10, 'CONTAGEM REGRESSIVA', '*' * 10)

for i in range (10, -1, -1):
    sleep(1.0)
    print(i)