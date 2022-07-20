"""
Escreva um programa que leia um valor em metros e
o exiba convertido em centímetros e milímetros.
"""


#  Criando um dicionário para armazenar as cores
cores = {'limpa': '\033[m',
         'v': '\033[1;31m',
         'a': '\033[1;33m'}
n = float(input('Digite um valor em metros: '))
print(f'{cores["v"]}{n}m {cores["limpa"]}corresponda a {cores["a"]}{n / 1000}km')
print(f'{cores["v"]}{n}m {cores["limpa"]}corresponda a {cores["a"]}{n / 100}hm')
print(f'{cores["v"]}{n}m {cores["limpa"]}corresponda a {cores["a"]}{n / 10}dam')
print(f'{cores["v"]}{n}m {cores["limpa"]}corresponda a {cores["a"]}{n * 10}dm')
print(f'{cores["v"]}{n}m {cores["limpa"]}corresponda a {cores["a"]}{n * 100}cm')
print(f'{cores["v"]}{n}m {cores["limpa"]}corresponda a {cores["a"]}{n * 1000}mm')
