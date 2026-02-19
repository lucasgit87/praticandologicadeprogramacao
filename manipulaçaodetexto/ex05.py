fr = input('Digite uma frase: ').strip().upper()
contador = fr.count('A')
primeiro = fr.find('A')+1
ultima = fr.rfind('A')+1
print(f'Na frase {fr} \n A letra (A) aparece {contador} \n a primeira letra (A) aparece na prosição {primeiro} \n já última letra (A) aparece na {ultima} posição.')