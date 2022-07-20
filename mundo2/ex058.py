"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em
um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
"""


from random import randint
print('\033[1;31m-=-\033[m'*10)
print('Jogo da Adivinhação')
print('\033[1;31m-=-\033[m'*10)
num_usuario = 0
num_comp = randint(0, 10)
cont = 0
while num_usuario != num_comp:
    num_usuario = int(input('Digite um número entre 0 e 10: '))
    cont = cont + 1
    if num_usuario < num_comp:
        print('\033[1;36mMais...\nTente novamente\033[m')
    else:
        print('\033[1;36mMenos...\nTente novamente\033[m')
print(f'Você acertou! O número pensado foi \033[1;31m{num_comp}\033[m')
print(f'Foram feitas {cont} tentativas.')


