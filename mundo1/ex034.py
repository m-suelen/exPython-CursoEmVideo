"""
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a
R$1250,00, calcule um aumento de 10%. Para os inferiores
ou iguais, o aumento é de 15%.
"""


salario = float(input('Informe o salário do funcionário: '))
if salario > 1250.00:
    novo_salario = salario + (salario * 10) / 100
else:
    novo_salario = salario + (salario * 15) / 100
print(f'O salário de R${salario:.2f} passará a ser de R${novo_salario:.2f}')

