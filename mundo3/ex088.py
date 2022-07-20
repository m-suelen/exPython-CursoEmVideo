"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""


from random import randint
from time import sleep
numeros = []
jogos = []
print(f'{" MEGA SENA ":=^30}')
print('='*30)
qntd = int(input('Quantos Jogos vc quer? '))
tot = 1
while tot <= qntd:
    cont = 1
    while cont <= 6:
        num = randint(1, 61)
        if num not in numeros:
            numeros.append(num)
            cont += 1
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    tot += 1
print(f'Sorteando {qntd} Jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('Boa sorte')



