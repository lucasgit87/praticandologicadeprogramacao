import random
from time import sleep
num = random.randint(1, 5)
numaadv = int(input("Digite um número de (1 a 5): "))
print('Analisando...')
sleep(3)
if numaadv == num:
    print(f'Você Acertou! O Número digitado foi {numaadv} o número gerado foi {num}')
else:
    print(f'Você Errou! O Número digitado foi {numaadv} o número gerado foi {num}')
