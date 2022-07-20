"""
Faça um programa que leia algo pelo teclado e
mostre na tela o seu tipo primitivo e todas
as informações possíveis sobre ele.
"""


a = input('Digite algo: ')
print('O tipo é primitivo', '\033[m', type(a))
print('Só tem espaços?', '\033[m', a.isspace())
print('É um número?', '\033[m', a.isnumeric())
print('É alfabético?', '\033[m', a.isalpha())
print('É alfanumérico?', '\033[m', a.isalnum())
print('Está em maiusculas?', '\033[m', a.isupper())
print('Está em minusculas?', '\033[m', a.islower())
print('Está capitalizada?', '\033[m', a.istitle())
