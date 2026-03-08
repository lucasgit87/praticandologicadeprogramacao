n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite o segundo número: '))
m = (n1 + n2)/2
if m <= 6.0:
    print(f'Sua media foi {m}. Você está reprovado!')
else:
    print(f' Sua media foi {m}. Você está aprovado!')