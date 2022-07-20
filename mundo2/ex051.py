"""
Desenvolva um programa que leia o primeiro termo e
a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
"""


prim = int(input('Digite o 1° termo: '))
r = int(input('Digite a razão: '))
decimo = prim + (10 - 1) * r
for c in range(prim, decimo + r, r):
    print(f'{c}', end=' -> ')
print('Acabou!')








