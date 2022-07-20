"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma
lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.
"""


numeros = []
posmaior = []
posmenor = []
for i in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))
for c, n in enumerate(numeros):
    if n == max(numeros):
        posmaior.append(c)
    elif n == min(numeros):
        posmenor.append(c)
print('='*30)
numeros.sort()
print(f'Os valores digitados foram {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições', end=' ')
for n in posmaior:
    print(n, end='..')
print(f'\nO menor valor digitado foi {min(numeros)} nas posições', end=' ')
for n in posmenor:
    print(n, end='..')




