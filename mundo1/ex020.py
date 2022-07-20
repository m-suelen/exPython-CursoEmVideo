"""
O mesmo professor do desafio 19 quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""


from random import shuffle
nome1 = input('1°aluno: ')
nome2 = input('2°aluno: ')
nome3 = input('3°aluno: ')
nome4 = input('4°aluno: ')
alunos = [nome1, nome2, nome3, nome4]
shuffle(alunos)  # shuffle para embaralhar uma lista
print('A ordem de apresentação será: ')
print('\033[1;31;43m', alunos, '\033[m')
