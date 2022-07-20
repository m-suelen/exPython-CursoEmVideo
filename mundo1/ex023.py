"""
Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados.
"""


num = int(input('Digite um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'Unidade: \033[1;33m{unidade}\033[m \nDezena: \033[31m{dezena}\033[m '
      f'\nCentena: \033[1;35m{centena}\033[m \nMilhar: \033[1;36m{milhar}')
