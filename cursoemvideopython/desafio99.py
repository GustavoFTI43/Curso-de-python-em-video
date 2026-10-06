from cordes import desafio,quebra_de_linha
desafio(99)
                # crie uma função chamda maior
                # ela vai receber varios parametros com valores inteiros
                # a função tem que analizar todos parametros e fizer qual o maior
from time import sleep
def maior(valores):
    print(quebra_de_linha)
    print('Analizando os valores passados ...')
    for va in valores:
            print(va , end=' ' , flush=True)
            sleep(0.5)
    print(f' Foram infomados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {max(valores)}')

'''
from random import randint
for r in range(5):
    numeros = list()
    for n in range(randint(1 , 6)):
        numero = randint(0 , 100)
        numeros.append(numero)
    sleep(2)
    maior(numeros)
'''
# jeito do guanabara
# meu codigo nao recebe nenhum valor e recebe em lista
def maior1(*parametros):
    print(quebra_de_linha)
    print('Analizando os valores passados ...')
    cont = maiorn = 0
    for n in parametros:
        print(n , end= ' ' , flush=True)
        sleep(1)
        if cont == 0 :
            maiorn = n 
        if n > maiorn:
            maiorn = n
        cont += 1
    print(f' Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maiorn}')

maior1()        # o python aceita esta chamada de função sem parametro apenas pq o parametro para esta função esta em modo de desempacotar com >> *