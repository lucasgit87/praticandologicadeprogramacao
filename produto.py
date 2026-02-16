print('======Tabela de produtos=========')
print('- PRODUTO           - QTD _ STATUS    = VALOR    -')
print('==================================================')
print('- Papel A4          - 50  _ Disponível = R$ 25,00 -')
print('- Caneta Azul       - 100 _ Disponível = R$ 2,50  -')
print('- Grampeador        - 05  _ Esgotado   = R$ 45,00 -')
print('--------------------------------------------------')
print ('_ Total em Estoque: 155 itens                    _')
print('==================================================')
pro = input('Escolha um produto: ')
pre = float(input('Digite o valor do produto: '))
des = pre * 0.05
prodes = pre - des

print(f'{pro} com valor de R${pre} com 5% fica {prodes}')