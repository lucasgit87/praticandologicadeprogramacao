from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print(f'Atleta mirin')
elif idade <= 14:
    print(f'Atleta infantil')
elif idade <= 19:
    print('Atleta junior')
elif idade <= 25:
    print(f'Atleta Sênior')
else:
    print('Atleta master')

