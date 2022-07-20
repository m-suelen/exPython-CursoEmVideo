"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""


pessoa = dict()
pessoas = list()
soma = media = 0
while True:
    pessoa.clear()
    print('-=' * 10)
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo (M/F): ')).strip().upper().split()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        continuar = str(input('Continuar (S/N)? ')).strip().upper().split()[0]
        if continuar in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if continuar == 'N':
        break
media = soma / len(pessoas)
print('*'*25)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'[{p["nome"]}]', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'   {k} = {v};', end='')
        print()











