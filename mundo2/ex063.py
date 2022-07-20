"""
Escreva um programa que leia um número N inteiro
qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
"""


t1 = 0
t2 = 1
t3 = 0
num = int(input('Digite um número: '))
cont = 3
print(f'{" FIBONACCI ":=^30}')
print(t1, t2, end=' ')
while cont <= num:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    cont += 1




