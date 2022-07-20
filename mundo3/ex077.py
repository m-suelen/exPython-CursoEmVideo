"""
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
"""


palavras = ('dormir', 'ler', 'estudar', 'comer', 'correr', 'andar',
            'nadar', 'praticar', 'aprender', 'brincar', 'viajar')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} tem a vogal', end='..')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


