"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""


tabela = ('Palmeiras', 'Corinthians', 'Internacional', 'Atlético-PR',
          'São Paulo', 'Atlético-MG', 'Chapecoense', 'Santos', 'Bragantino',
          'Flamengo', 'Fluminense', 'Coritiba', 'América-GO', 'Boatafogo',
          'Ceará SC', 'Goiás', 'Atlético-GO', 'Cuiaba', 'Juventude', 'Fortaleza')
print(f'Os times do Brasileirão são {tabela}')
print('='*20)
print(f'Os primeiros 5 colocados são: {tabela[0:5]}')
print('='*20)
print(f'Os últimos 4 colocados são : {tabela[-4:]}')
print('='*20)
print(f'Tabela em ordem alfabética: {sorted(tabela)}')
print('='*20)
pos = tabela.index('Chapecoense')
print(f'O time Chapecoense se encontra na posição {pos + 1}°')



