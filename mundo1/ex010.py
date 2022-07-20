"""
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos dólares ela pode comprar.
"""


reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolares = reais / 3.27
print(f'Com R${reais:.2f} você pode comprar \033[1;31mUS${dolares:.2f}\033[m dólares')
