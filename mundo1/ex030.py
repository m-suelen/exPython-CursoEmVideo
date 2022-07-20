"""
Crie um programa que leia um número inteiro e
mostre na tela se ele é PAR ou ÍMPAR.
"""


num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print(f'O número \033[4;33m{num}\033[m é Par!')
else:
    print(f'O número \033[4;35m{num}\033[m é Ímpar!')

