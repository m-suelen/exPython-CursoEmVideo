"""
Crie um programa onde o usuário digite uma expressão qualquer que
use parênteses. Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta.
"""


verifica = []
exp = input('Digite uma expressão: ')
for simb in exp:
    if simb == '(':
        verifica.append(simb)
    elif simb == ')':
        if len(verifica) > 0:
            verifica.pop()
        else:
            verifica.append(simb)
            break
print('A expressão está válida' if len(verifica) == 0 else 'Expressão inválida')
