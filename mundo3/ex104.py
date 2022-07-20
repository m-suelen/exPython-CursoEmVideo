"""
Crie um programa que tenha a função leiaInt(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo
a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
"""


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro! Digite apenas números\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print('\033[1;36mVocê acabou de digitar o número\033[m', n)



