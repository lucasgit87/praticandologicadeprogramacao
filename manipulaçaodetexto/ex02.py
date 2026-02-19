num = int(input('Digite qualquer número interio: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mi = num // 1000 % 10
print(f'O número digitado tem {num} tem \n {uni} unidade \n {dez} dezena \n {cen} centena \n {mi} milhar')