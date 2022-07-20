"""
Crie um programa que leia o ano de nascimento de
sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.
"""


from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano_nasc = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Há {totmaior} pessoas maiores de idade e {totmenor} menores de idade')
