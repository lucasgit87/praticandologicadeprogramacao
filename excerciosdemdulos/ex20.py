import random

alunos = ['Ana', 'Bruno', 'Caio', 'Duda', 'Lucas','Lúcio','Thiago','Hermes','Nathan','Giovania']
res = random.choices(alunos, k =4)
print(f'A ordem de apresentação foi: {res}')


