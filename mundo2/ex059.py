"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""


from time import sleep
print('Informe dois valores')
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
opcao = 0
while opcao != 5:
    print('Escolha uma das opções abaixo: ')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior número
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Qual a sua opcão? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'\033[1;33m{n1} + {n2} = {soma}\033[m')
    elif opcao == 2:
        mult = n1 * n2
        print(f'\033[1;33m{n1} x {n2} = {mult}\033[m')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'\033[1;33mO maior número é {maior}\033[m')
    elif opcao == 4:
        print('Informe os novos números: ')
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
    elif opcao == 5:
        print('\033[1;35mFinalizando!\033[m')
    else:
        print('Opção inválida. Tenten novamente')
    print('-=' * 15)
    sleep(1)
print('Fim do programa!')










