"""
Faça um programa que leia a largura e a altura de uma
parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta uma área de 2 metros quadrados.
"""


larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
a = larg * alt
print(f'A área total é de {a} metros quadrados. Você precisará de {a / 2}l de tintas')
