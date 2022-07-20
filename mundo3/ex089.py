"""
Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
"""


boletim = []
continuar = 's'
cont = 1
print(f'{" BOLETIM ESCOLAR ":=^30}')
while continuar != 'n':
    print('-' * 25)
    print(f'{cont}° Aluno')
    nome = str(input('Nome: '))
    n1 = float(input('1° Nota: '))
    n2 = float(input('2° Nota: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    continuar = str(input('Coninuar (s/n)? ')).strip().lower().split()[0]
    cont += 1
print('='*30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('='*30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>6.1f}')
while True:
    print('='*30)
    opc = int(input('Mostrar nostas de qual aluno? (999) para sair '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')





