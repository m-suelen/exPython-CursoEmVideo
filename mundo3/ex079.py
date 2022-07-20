"""
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
"""


numeros = []
continuar = 's'
while continuar != 'n':
    num = (int(input('Digite um valor: ')))
    if num in numeros:
        print('Valor duplicado. Não será adicionado')
    else:
        numeros.append(num)
        print('Valor adicionado com sucesso!')
    continuar = str(input('Você quer continuar (s/n)? ')).strip().lower().split()[0]
print('='*30)
numeros.sort()
print(f'Os valores digitados foram {numeros}')




