from cordes import desafio, quebra_de_linha
desafio(102)
                # crie uma função chamada farorial
                # receba 2 valores como parametreo um para calcular fatorial e outro para caso queria mostrar a conta fatorial
                # retorne o valor fatorial

def fatorial(n , show = False):
    '''
    => calcula o valor fatorial de um numero.
    n : para numero a ser calculado.
    show : se true (mostra conta fatorial) é opcional.
    return : valor fatorial de n.
    '''
    b = 1
    for i in range(n , 0 , -1):
        if show == True :
            if i == 1:
                print(f'{i} =', end=' ')
            else:
                print(f'{i} X', end=' ')
        b *= i
    return b
print(quebra_de_linha)
help(fatorial)
