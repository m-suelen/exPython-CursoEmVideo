"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas;
– Quantas letras ao todo (sem considerar espaços);
– Quantas letras tem o primeiro nome.
"""

nome = str(input('Informe o seu nome completo: ')).strip()
print(f'Seu nome com as letras maiúsculas: \033[1;31m{nome.upper()}\033[m')
print(f'Seu nome com as letras minúsculas: \033[1;31m{nome.lower()}\033[m')
print(f'Seu nome tem ao todo \033[4;35m{len(nome) - nome.count(" ")} letras')  # conta a qntd de espaços e remove
dividido = nome.split()
print(f'\033[mO seu primeiro nome é \033[1;32m{dividido[0]}\033[m', end=' ')
print(f'e tem \033[1;33m{len(dividido[0])}\033[m letras ')
