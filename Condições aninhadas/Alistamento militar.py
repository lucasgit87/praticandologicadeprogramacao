from datetime import date
atual = date.today().year
ano = int(input('Digite o ano que você nasceu: '))
idade = atual - ano
falta =  18 - idade
ano_de_alistamento = atual + falta
if idade < 18:
    print(f'Nascido em {ano}.\n Você tem {idade}. \n Ainda é menor de idade.\n Ainda falta {falta} anos para o alistamento.\n Seu alistamento será em {ano_de_alistamento}.')
elif idade == 18:
    print(f'Você tem {idade}. Você deve se alista esse ano.')
elif idade > 18:
    print(f'você tem {idade}. Já deveria ter se alistado.')