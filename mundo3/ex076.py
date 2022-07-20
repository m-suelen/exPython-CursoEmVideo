"""
Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. No final, mostre uma
listagem de preços, organizando os dados em forma tabular.
"""


listagem = ('Caderno', 15.20, 'Mochila', 30, 'Caneta', 3.10, 'Lápis', 2,
            'Estojo', 7.50, 'Livro', 25.90, 'Cola', 8.70, 'Borracha',
            5, 'Apontador', 4.20)
print('='*40)
print(f'{" Papelaria Estrela ":^40}')
print('='*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('='*40)









