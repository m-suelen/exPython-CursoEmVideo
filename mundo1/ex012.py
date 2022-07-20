"""
Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.
"""


prod = input('Informe o produto: ')
valor = float(input('Valor do produto: R$'))
nv = valor - (valor * 5 / 100)
print(f'O produto {prod} que custava {valor} sairá por R${nv:.2f} com 5% de desconto')
