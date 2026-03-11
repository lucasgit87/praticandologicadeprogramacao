from time import sleep
num = int(input('Digite um número inteiro: '))
print('Analisando...')
sleep(1)
print('Escolha uma das opções abaixo: ')
print('-1 para binário')
print('-2 para octal')
print('-3 para hexadecimal')
a = int(input('Digite a opção escolhida: '))
print('Processando...')
sleep(2)
bi = bin(num)
oc = oct(num)
he = hex(num)
if a == 1:
    print(f'O número {num} convertido para binário fica {bi}')
elif a == 2:
    print(f'O número {num} convertido para octal fica {oc}')
elif a == 3:
    print(f'O número {num} convertido para hexadecimal fica {he}')



