"""
Aprimore o desafio 93 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""


jogador = dict()
total = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    total.clear()
    for c in range(0, partidas):
        total.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = total[:]
    jogador['total'] = sum(total)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Continuar (S/N)? ')).strip().upper().split()[0]
        if continuar in 'SN':
            break
        print('Erro! Responda S ou N')
    if continuar == 'N':
        break
    print('='*40)
print('-'*40)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print('-'*40)
        print(f'Levantamento do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
print('-'*40)


