"""
Melhore o DESAFIO 61, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa
encerrará quando ele disser que quer mostrar 0 termos.
"""


prim = int(input('Digite o 1° termo: '))
r = int(input('Digite a razão: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' -> ')
        termo += r
        cont += 1
    print('Pausa..')
    mais = int(input('Quantos termos quer mostrar a mais (0 para sair)? '))
print(f'Progressão finalizada com {total} termos mostrados')


