"""
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.
"""


valor = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o salário do comprador: R$'))
ano = int(input('Quantos anos deseja pagar? '))
prestacao_limite = salario - (salario * 30) / 100
prestacao = valor / (ano * 12)
if prestacao > prestacao_limite:
    print('A prestação excedeu 30% do salário. Empréstimo negado!')
else:
    print(f'A prestação das parcelas será de {prestacao:.2f}R$')

