"""
Faça um programa que tenha uma função chamada contador(), que
receba três parâmetros: início, fim e passo. Seu programa
tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""


from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)
            sleep(0.2)
    else:
        for c in range(i, f-1, -p):
            print(c, end=' ', flush=True)
            sleep(0.2)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('='*43)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
inc = int(input('Passo: '))
contador(ini, fim, inc)

