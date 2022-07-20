"""
Escreva um programa que converta uma temperatura digitando
em graus Celsius e converta para graus Fahrenheit.
"""


c = float(input('Digite uma valor em graus Celsius: '))
f = ((c * 9) / 5) + 32
print(f'A temperatura de \033[1;31m{c:.1f}°C\033[m corresponde a \033[1;33m{f:.1f}°F')
