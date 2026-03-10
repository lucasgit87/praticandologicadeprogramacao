salario = float(input("Digite o salário: R$ "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f"Novo salário: R$ {novo:.2f}")
