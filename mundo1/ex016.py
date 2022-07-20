"""
Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção Inteira.
"""


from math import trunc
num = float(input('Digite um número: '))
print(f'A parte inteira de \033[0;31m{num}\033[m é \033[0;32m{trunc(num)}')
