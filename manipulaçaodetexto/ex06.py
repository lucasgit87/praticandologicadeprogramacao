nome_completo = input('Digite seu nome completo: ').upper().split()
primeironome = nome_completo[0].split()
ultimonome = nome_completo[len(nome_completo)-1]
print(f'Seu primeiro nome é {primeironome} \nSeu ultimo nome é {ultimonome}.')