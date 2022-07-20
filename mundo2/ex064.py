"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).
"""


x = cont = soma = 0
num = int(input('Digite um número (999 para parar): '))
while x != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        x = 999
print(f'Foram digitados {cont} números e a soma é {soma}')

