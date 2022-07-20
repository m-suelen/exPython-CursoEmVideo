"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""


from time import sleep
print('Informe 3 segmentos de retas abaixo: ')
r1 = float(input('Digite o 1° valor: '))
r2 = float(input('Digite o 2° valor: '))
r3 = float(input('Digite o 3° valor: '))
print('\033[1;33mANALISANDO...\033[m')
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[4;35mAs três retas podem formar um Triângulo\033[m', end='')
    if r1 == r2 == r3:
        print('\033[4;35m Equilátero\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[4;35m Escaleno\033[m')
    else:
        print('\033[4;35m Isósceles\033[m')
else:
    print('\033[4;35mAs três retas NÃO podem formar um Triângulo\033[m')

