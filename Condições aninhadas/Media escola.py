n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media < 5:
    print(f'Aluno reprovado com média {media:.1f}')
elif 5 <= media < 7:
    print(f'Aluno ficou de recuperação com média {media:.1f}')
else:
    print(f'Aluno aprovado com média {media:.1f}')