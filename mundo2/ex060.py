"""
Faça um programa que leia um número qualquer e
mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""


num = int(input('Digite um número: '))
print(f'\033[1;31m{num}!\033[m = ', end='')
fat = 1
while num != 0:
    print(num, end='')
    print(' x ' if num > 1 else ' =', end='')
    fat *= num
    num -= 1
print('\033[1;33m', fat)

