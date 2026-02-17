km = int(input('Digite a quantidade de quilometros(KM) percorridos:  '))
qdia = int(input('Digite a quantidade de dias que o carro foi alugado: '))
preapagar = (km * 0.15 ) + (qdia * 60 )
print(f'O carro alugado por {qdia} dias percorreu {km}km dando R${preapagar} a serem pagos.')