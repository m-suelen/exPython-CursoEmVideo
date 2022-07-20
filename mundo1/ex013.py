"""
Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.
"""


sal = float(input('Informe o salário do Funcionário: R$'))
nsal = sal + (sal * 15 / 100)
print(f'O salário de R${sal:.2f} com 15% de aumento será de \033[1;31;47mR${nsal:.2f}\033[m')
