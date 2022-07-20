"""
Faça um programa que leia uma frase pelo teclado e mostre quantas
vezes aparece a letra “A”, em que posição ela aparece a primeira
vez e em que posição ela aparece a última vez.
"""


frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra "A" aparece: {frase.count("A")} na frase')
print(f'A letra "A" aparece pela primeira vez na posição: {frase.find("A")+1} da frase')
print(f'A letra "A" aparece pela última vez na posição: {frase.rfind("A")+1} da frase')



