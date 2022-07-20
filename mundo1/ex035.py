"""
Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.
"""


from time import sleep
print('Informe 3 segmentos de retas abaixo: ')
r1 = float(input('Digite o 1° valor: '))
r2 = float(input('Digite o 2° valor: '))
r3 = float(input('Digite o 3° valor: '))
print('\033[1;33mANALISANDO...\033[m')
sleep(1)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[4;35mAs três retas podem formar um Triângulo.\033[m')
else:
    print('\033[4;31mNão é possível formar um triângulo.')
