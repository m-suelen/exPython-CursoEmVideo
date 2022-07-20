"""
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""


#  Utilizando o if simplificado
dist = float(input('Informe a distância da sua viagem: Km '))
valor = dist * 0.50 if dist <= 200 else dist * 0.45
print(f'O valor da passagem será de R${valor}')


