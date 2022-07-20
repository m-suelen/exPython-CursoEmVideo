"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é
o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""


soma_idade = contm = media_idade = maior_idade = 0
nome_maior = ''
for c in range(1, 5):
    print(f'==== {c}° Pessoa ====')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    soma_idade += idade
    media_idade = soma_idade / c
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_maior = nome
    if sexo in 'Ff' and idade < 21:
        contm += 1
print('='*30)
print(f'A média de idade do grupo é de {media_idade:.2f}')
print(f'O Homem mais velho tem {maior_idade} anos e se chama {nome_maior}')
print(f'Há {contm} Mulheres menores de 21 anos')




