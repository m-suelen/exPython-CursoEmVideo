"""
Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com a sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora exata de se alistar ou se já
passou do tempo do alistamento. Seu programa também deverá
mostrar o tempo que falta ou que passou do prazo.
"""


from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Informe o ano de nascimento: '))
idade = ano_atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem a idade de {idade} anos')
sexo = str(input('Qual o seu gênero (M/F)? '))
if sexo == 'M':
    if idade == 18:
        print('Está na hora de você se alistar!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Faltam {saldo} anos para você se alistar')
        ano_alist = ano_atual + saldo
        print(f'Você deverá se alistar em {ano_alist}!')
    else:
        saldo = idade - 18
        print(f'Passou {saldo} anos do prazo do alistamento')
        ano_alist = ano_atual - saldo
        print(f'Seu alistamento foi em {ano_alist}!')
else:
    print('Você não precisa se alistar!')


