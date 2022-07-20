"""
Crie um programa que tenha uma dupla totalmente preenchida com
uma contagem por extenso, de zero até vinte. Seu programa deverá
ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""


contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

continuar = 's'
while continuar != 'n':
    num = int(input('Digite um número entre 0 e 20: '))
    while not num >= 0 or not num <= 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {contagem[num]}')
    continuar = str(input('Você quer continuar (s/n)? ')).strip().lower().split()[0]

