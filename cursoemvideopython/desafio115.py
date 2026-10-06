from cordes import desafio,cores
desafio(115)
from pkdesafios.exe115 import *
from time import sleep



while True:
    arq = 'exer115.txt'
    if not arqExiste(arq):
        criarArq(arq)
    resp = menu(['Pessoas Cadastradas' , 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        tituloformatado('NOVO CADASTRO' , 2)
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('idade: ')
        cadastrar(arq , nome , idade)
    elif resp == 3:
        print(f'\033[33m{"Saindo do Sitema .... Até Logo !":^54}\033[m')
        break
    else:
        print(f'\033[31mErro digite uma opção valida\033[m')
    sleep(1)