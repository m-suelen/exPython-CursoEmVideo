"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""


print('='*20)
print('Cadastro de Pessoas')
print('='*20)
cont = contm = contf = 0
while True:
    print('Novo cadastro')
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Sexo (M/F): ')).strip().upper().split()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F' and idade < 20:
        contf += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar (S/N): ')).strip().upper().split()[0]
    if continuar == 'N':
        break
print('-' * 20)
print(f'Há {cont} pessoas com mais de 18 anos')
print(f'Foram cadastrados {contm} Homens')
print(f'Há {contf} Mulheres com menos de 20 anos')
