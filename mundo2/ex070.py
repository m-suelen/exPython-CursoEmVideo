"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""


print(f'{" Loja Downtown ":=^25}')
cont = maior = menor = soma = 0
prod_barato = ''
while True:
    nome_prod = str(input('Nome do produto: '))
    preco_prod = float(input('Preço do produto: R$'))
    cont += 1
    soma += preco_prod
    if preco_prod > 1000:
        maior += 1
    if cont == 1 or preco_prod < menor:
        menor = preco_prod
        prod_barato = nome_prod
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Continuar (S/N): ')).strip().upper().split()[0]
    if continuar == 'N':
        break
print('-'*20)
print(f'O valor total da compra é de {soma:.2f}R$')
print(f'Há {maior} produtos que custam mais de 1000.00R$')
print(f'O produto mais barato foi {prod_barato} que custa {menor:.2f}R$')
