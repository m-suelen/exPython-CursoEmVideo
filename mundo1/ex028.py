"""
Escreva um programa que faça o computador “pensar” em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa
deverá escrever na tela se o usuário venceu ou perdeu.
"""


from random import randint
from time import sleep
print('\033[1;31m-=-\033[m'*10)
print('Jogo da Adivinhação')
print('\033[1;31m-=-\033[m'*10)
num_usuario = int(input('Digite um número entre 0 e 5: '))
num_comp = randint(0, 5)
print('\033[1;36mPROCESSANDO...\033[m')
sleep(1)
if num_usuario == num_comp:
    print(f'Você acertou! O número pensado foi \033[1;33m{num_comp}\033[m')
else:
    print(f'O número pensado foi \033[1;33m{num_comp}\033[m. Tente novamente')

