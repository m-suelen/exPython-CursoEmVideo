"""
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados e
também indique o menor e o maior valor que estão na tupla.
"""


from random import randint
aleatorios = tuple()
cont = 1
while cont <= 5:
    aleatorio = randint(1, 6)
    aleatorios += aleatorio,
    cont += 1
print(f'Os números sorteados foram {aleatorios}')
print(f'O maior número da lista é {max(aleatorios)}')
print(f'O menor número da lista é {min(aleatorios)}')
