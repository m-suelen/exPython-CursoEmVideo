"""
Faça um programa que leia um número inteiro e
diga se ele é ou não um número primo.
"""


num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;33m', end=' ')
        tot += 1
    else:
        print('\033[1;31m', end=' ')
    print(c, end=' ')
print(f'\033[m\nO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('O número é PRIMO')
else:
    print('O número NÃO É PRIMO')

