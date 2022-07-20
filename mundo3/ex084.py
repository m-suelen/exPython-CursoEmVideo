"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""


pessoas = []
dado = []
maior = menor = 0
cont = 1
continuar = 's'


print(f'{" Cadastro de Pessoas ":=^30}')
while continuar != 'n':
    print('-'*20)
    print(f'{cont}° Pessoa')
    dado.append(str(input('Nome: ')))
    dado.append((float(input('Peso: '))))
    if cont == 1:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    continuar = str(input('Continuar (s/n)? ')).strip().lower().split()[0]
    cont += 1
print('='*30)
print(f'Ao todo foram cadastradas {cont - 1} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O menor peso de foi de {menor}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')







