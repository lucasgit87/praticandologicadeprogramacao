nome = input('Digite seu nome completo: ').strip()
contador = len(nome) - nome.count(' ')
primeronome = len(nome.split()[0])
letraminuscula = nome.lower()
letramaiuscula = nome.upper()
print(f'O seu nome completo é {nome} \n Ao total seu nome tem {contador} letras \n Seu primero nome tem {primeronome} letras \n Seu nome em maiusculo é {letramaiuscula} \n  é o seu nome em minusculo é {letraminuscula}')

