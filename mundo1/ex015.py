"""
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0,15 por Km rodado.
"""


km = float(input('Informe a quantidade de km percorridos: '))
d = int(input('Informe a quantidade de dias: '))
p = (60 * d) + (0.15 * km)
print(f'O preço total a pagar pelo carro alugado é de \033[1;31;46mR${p:.2f}\033[m')
