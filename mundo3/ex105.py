"""
Faça um programa que tenha uma função notas() que pode
receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""


def notas(*n, sit=False):
    """
    -> Função para anilisar notas e situação de vários alunos.
    :param n: Aceita várias notas dos alunos.
    :param sit: Valor opcional, indicando se deve ou não mostrar a situação.
    :return: Dicionário com as informações dos alunos.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    soma = sum(n) / len(n)
    r['media'] = ('{:.2f}'.format(soma))
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoável'
        else:
            r['situacao'] = 'Ruim'
    return r


resp = notas(3.5, 2, 4, 7)
print(resp)
help(notas)


