"""
Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário. Se por acaso
a CTPS for diferente de ZERO, o dicionário receberá também o ano
de contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.
"""


from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - ano_nasc
pessoa['ctps'] = int(input('Cateira (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['ano'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['apossentadoria'] = (pessoa['ano'] + 35) - ano_nasc
print('='*30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
