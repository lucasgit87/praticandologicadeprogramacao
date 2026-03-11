r1 = float(input('Digite o primeiro comprimento: '))
r2 = float(input('Digite o segundo comprimento: '))
r3 = float(input('Digite o terceiro comprimento: '))
if r1 + r2 > r3:
    if r2 + r1 < r3:
        pass
    else:
        if r3 + r1 < r2:
            pass
        else:
         print('Pode formar um triangulo!')
else:
    print('Não pode forma um triangulo!')