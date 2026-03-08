from time import sleep
disviagem = int(input('Digite a distancia da viagem: '))
print('Calculando...')
sleep(2)
viagemc = disviagem * 0.50
viageml = disviagem * 0.45
if disviagem <= 200:
    print(f'A distacia foi de 200km, o valor a ser pago será R$ {viagemc}.')
else:
    print(f'A distacia foi mais de 200km, o valor a ser pago será R$ {viageml}.')