"""
Refaça o DESAFIO 51, lendo o primeiro termo e a
razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
"""


prim = int(input('Digite o 1° termo: '))
r = int(input('Digite a razão: '))
decimo = prim + (10 - 1) * r
while prim != decimo + r:
    print(f'{prim}', end=' -> ')
    prim += r
print('Acabou!')


