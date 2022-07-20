"""
Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""


lista_num = ()
cont = 1
while cont <= 4:
    num = int(input('Digite um número: '))
    lista_num += num,
    cont += 1
print(f'Você digitou os valores {lista_num}')
print(f'O número 9 apareceu {lista_num.count(9)}x na lista')
if 3 in lista_num:
    print(f'O valor 3 apareceu na {lista_num.index(3) + 1}° posição')
else:
    print('O valor 3 não apareceu nenhuma vez')
print('Os valores pares digitados foram', end=' ')
for n in lista_num:
    if n % 2 == 0:
        print(n, end=' ')


