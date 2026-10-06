from cordes import desafio,quebra_de_linha
desafio(100)
                # crie uma lista chamda numeros
                # crie 2 funçoes para sorteio() e somapar()
                # sorteio ira sortear 5 numeros e guadar em uma lista
                # somapar vai somar todos valores pares que estao dentro da lista
from random import randint
from time import sleep
def sorteio(lista):
    print('Sorteando 5 valores da lista: ' , end='')
    for cont in range(5):
        n = randint(0,20)
        lista.append(n)
        print(f'{n} ', end='' , flush=True)
        sleep(1)
    print('Pronto !')

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista} , temos {soma}')

numeros = list()
sorteio(numeros)
somapar(numeros)
