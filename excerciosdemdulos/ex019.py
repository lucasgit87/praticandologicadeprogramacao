import random


dado = random.randint(1, 10)


alunos = ['Ana', 'Bruno', 'Caio', 'Duda']
sorteado = random.choice(alunos)

print(f"O dado caiu em: {dado}")
print(f"Quem vem apagar o quadro é: {sorteado}")