def leiadinheiro(msg):
    '''
    => faz a leitura apenas de valores numericos , recebe uma mensagem
    entrada para : input(msg) em loop até ser um valor numerico se nao retorna mensagem de erro
    return : valor em ponto flutuante
    '''
    while True:
        entrada = input(msg).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço invalido \033[m')
        else:
            return float(entrada)

def tituloformatado(txt , vezescr = 1):
    '''
    => recebe uma mensagem e quantidade de vezes que repetira o len(txt)
    cr para : somar o caracter total do txt formatado
    imprimi txt formatado com linhas para titulos
    '''
    cr = (len(txt) + 4) * vezescr
    print(f'{"=" * cr}\n{txt:^{cr}}\n{"=" * cr}')


