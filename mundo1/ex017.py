"""
Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
"""


from math import hypot
co = float(input('Qual o comprimento (m) do cateto oposto? '))
ca = float(input('Qual o comprimento (m) do cateto adjacente? '))
print(f'A hipotenusa será de {hypot(co, ca):.2f}')
