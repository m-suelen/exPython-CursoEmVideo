"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
"""


from random import randint
cont = 0
n_comp = randint(0, 10)
print('='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*30)
while True:
    n_jog = int(input('Digite um valor: '))
    s = n_jog + n_comp
    opcao = ''
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar (P/I): ')).strip().upper().split()[0]
    print('-'*30)
    print(f'Você jogou {n_jog} e o computador {n_comp}. Total {s}', end=' ')
    print('deu Par' if s % 2 == 0 else 'deu Ímpar')
    if opcao == 'P':
        if s % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif opcao == 'I':
        if s % 1 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar novamente...')
print('=' * 30)
print(f'Game Over você venceu {cont} vezes.')







