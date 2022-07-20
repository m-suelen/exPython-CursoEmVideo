"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas.
"""


numeros = []
pares = []
impares = []
continuar = 's'
while continuar != 'n':
    numeros.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar (s/n)? ')).strip().lower().split()[0]
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('='*30)
numeros.sort()
print(f'A lista completa é {numeros}')
print(f'A lista com os valores pares é {pares}')
print(f'A lista com os valores ímpares é {impares}')
