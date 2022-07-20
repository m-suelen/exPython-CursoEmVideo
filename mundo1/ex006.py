"""
Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.
"""


#  Utilizando a função Power para calcular a raiz quadrada
n = int(input('Digite um número: '))
print(f'O dobro de {n} é {n * 2}. \nO triplo é {n * 3}. \nA raiz quadrada é {pow(n, (1/2)):.2f}')

