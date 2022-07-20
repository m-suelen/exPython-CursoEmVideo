"""
Faça um programa que mostre a tabuada de vários números, um
de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo.
"""


print(f'{" TABUADA ":=^25}')
cont = 0
while True:
    n = int(input('Digite um valor: '))
    print('-'*20)
    if n < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{n} * {cont} = {n * cont}')
        cont += 1
print('Programa Tabuada Encerrado')















