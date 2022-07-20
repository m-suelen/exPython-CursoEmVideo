"""
Um professor quer sortear um dos seus quatro alunos para apagar
o quadro. Faça um programa que ajude ele, lendo o nome dos
alunos e escrevendo na tela o nome do escolhido.
"""


from random import choice
nome1 = input('1°aluno: ')
nome2 = input('2°aluno: ')
nome3 = input('3°aluno: ')
nome4 = input('4°aluno: ')
alunos = [nome1, nome2, nome3, nome4]  # Utilizando lista
escolhido = choice(alunos)
print(f'Aluno(a) escolhido(a) foi \033[1;30;42m{escolhido}\033[m')
