"""
Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome “SANTO”.
"""


cidade = str(input('Digite o nome da sua cidade: ')).strip()
print('\033[1;36mA cidade começa com "Santo"?\033[m ', cidade[:5].upper() == 'SANTO')

