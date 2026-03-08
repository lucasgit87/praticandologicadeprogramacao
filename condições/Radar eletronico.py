from time import sleep
vel = int(input('Qual foi a velocidade do veiculo? '))
print('Processando...')
sleep(2)
multa = (vel - 80) * 7
if vel > 80:
    print(f'Sua velocidade foi de {vel}km/h. Você foi multado em R$ {multa}.')
else:
    print(f'Sua velocidade foi de {vel}km/h. Veiculo dentro da velocidade permitida.')
