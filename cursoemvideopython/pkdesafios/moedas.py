from cordes import cores


def metade(valor , f = False):
    '''
    => recebe valor em dinheiro
    m para : dividir o valor
    f para : formataçao de valor
    return : m  if f == true: formatado. else: sem fromataçao
    '''
    m = valor / 2
    if f == True:
        return f'{real(m)}'
    else:
        return f'{m:.2f}'


def dobro(valor , f = False):
    '''
    => recebe valor em dinheiro
    d para : dobrar o valor
    f para : formataçao de valor
    return : d if f == true: formatado. else: sem fromataçao
    '''
    d = valor * 2
    return d if not f else real(d)  # condição simples


def aumentar(valor, p = 0 , f = False):
    '''
    => recebe valor em dinheiro
    a para : aumentar o valor
    p para : porcentagem recebida
    f para : formataçao de valor
    return : a if f == true: formatado. else: sem fromataçao
    '''
    a = valor + ((valor / 100) * p)
    if f == True:
        return f'{real(a)}'
    else:
        return f'{a:.2f}'


def diminuir(valor, p = 0 , f = False):
    '''
    => recebe valor em dinheiro
    di para : diminuir o valor
    p para : porcentagem recebida
    f para : formataçao de valor
    return : di if f == true: formatado. else: sem fromataçao
    '''
    di = valor - ((valor / 100) * p)
    if f == True:
        return f'{real(di)}'
    else:
        return f'{di:.2f}'
# criado para o desafio 108
def real(valor = 0, moeda = 'R$'):              # no começo fiz tranformando em uma string mais mudei para o jieto do guanabara
    return f'{moeda}{valor : .2f}'.replace('.',',')
    
# atualização chamando função de formatação(real) , dentro das outras funçoes para formatar automaticamente se desejado
def resumo(valor , aumento = 10 , redução = 5):
    '''
    => recebe valor em dinheiro 
    aumento para: receber a porcentagem para aumento(parametro opcional ;else 10)
    redução para : receber a porcentagem para redução(parametro opcional ;else 5) 
    "Imprimi um resumo com preço recebido contendo as função de dobro do preço,metade do preço,aumento do valor
    e redução do valor. todos com suas funçoes
    '''
    print(f'{"-" * 30}\n{"RESUMO DO VALOR": ^30}\n{"-" * 30}')
    print(f'Preço analisando: \t{real(valor)}')
    print(f'Dobro do preço: \t{dobro(valor , True)}')
    print(f'Metade do preço: \t{metade(valor,True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor , aumento , True)}')
    print(f'{redução}% de redução: \t{diminuir(valor , redução , True)}')
    print("-" * 30)
