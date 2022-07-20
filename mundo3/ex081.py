"""
Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""


numeros = []
continuar = 's'
while continuar != 'n':
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar (s/n)? ')).strip().lower().split()[0]
print('='*30)
print(f'Foram digitados {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é {numeros}')
if 5 in numeros:
    print('O valor 5 foi adicionado na lista')
else:
    print('O valor 5 não foi encontrado na lista')

