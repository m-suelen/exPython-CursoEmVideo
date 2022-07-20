"""
Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""

print(f'{" Lojas Suelen Store ":=^35}')
valor = float(input('Informe o valor do produto: R$'))
print('''Forma de Pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10) / 100
    print(f'O valor de R${valor:.2f} com 10% de desconto será de R${total:.2f}')
elif opcao == 2:
    total = valor - (valor * 5) / 100
    print(f'O valor de R${valor:.2f} com 5% de desconto será de R${total:.2f}')
elif opcao == 3:
    total = valor
    parcela = total / 2
    print(f'O valor de R${valor:.2f} terá parcelas de R${parcela:.2f} em 2x SEM JUROS')
elif opcao == 4:
    total = valor + (valor * 20) / 100
    num_parcela = int(input('Quantas parcelas? '))
    parcela = total / num_parcela
    print(f'O valor de R${valor:.2f} terá parcelas de R${parcela:.2f} em {num_parcela}x COM JUROS')
else:
    total = valor
    print('\033[1;31mOpcão inválida. Tente novamente!\033[m')
print(f'A compra de R${valor:.2f} no final ficará R${total:.2f}')









