valorcasa = float(input('Digite o valor da casa: R$  '))
salario = float(input('Digite sua renda mensal: R$ '))
parcelas = int(input('Digite em quanto tempo pretende paga o imovel: '))
pre = valorcasa/(parcelas*12)
min = salario * 30 / 100
print(f'Para pagar um casa de R${valorcasa:.2F} em {parcelas} anos a prestação será de {pre}.')
if pre <= min:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo não podera ser concedido!')