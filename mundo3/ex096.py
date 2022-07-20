"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def area(a, b):
    result = a * b
    print(f'A área de um terreno {a}x{b} é de {result} metros quadrados')


print('~'*30)
print(f'{" Controle de Terrenos ":=^30}')
print('~'*30)
largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))
area(largura, altura)
