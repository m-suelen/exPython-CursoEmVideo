"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""


nome = str(input('Digite o seu nome completo: ')).strip()
dividido = nome.split()
print(f'Seu primeiro nome: \033[1;35m{dividido[0]}\033[m')
print(f'Seu último nome: \033[1;36m{dividido[-1]}')
