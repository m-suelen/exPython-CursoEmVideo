"""
Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
frase_junta = ''.join(frase)
frase_inverte = ''
for letra in range(len(frase_junta)-1, -1, -1):
    frase_inverte += frase_junta[letra]
print(f'O inverde {frase_junta} é {frase_inverte}')
if frase_inverte == frase_junta:
    print('Temos um palíndromo!')
else:
    print('NÂO forma um palíndromo!')










