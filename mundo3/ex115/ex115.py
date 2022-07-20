"""
Mini projeto: banco de dados
- Criar um menu
- Acessando arquivos
"""


from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        #  Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        #  Opção de cadastrar uma nova pessoa
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do programa...')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')
    sleep(1)








