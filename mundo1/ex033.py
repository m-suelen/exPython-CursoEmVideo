"""
Faça um programa que leia três números e
mostre qual é o maior e qual é o menor.
"""


n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
#  Verifica o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#  Verifica o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O número \033[1;30;44m {menor} \033[m é o menor')
print(f'O número \033[1;30;45m {maior} \033[m é o maior')

