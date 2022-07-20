"""
Escreva um programa que leia a velocidade de um carro. Se ele
ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""


v = float(input('Informe a velocidade percorrida: '))
if v > 80:
    m = (v - 80) * 7
    print(f'O motorista excedeu o limite de 80Km. A multa será de R${m:.2f}')
print('Dirija com segurança. Tenha um bom dia!')
