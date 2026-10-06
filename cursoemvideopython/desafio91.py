from cordes import desafio,quebra_de_linha
                # receba 4 numeros aleatorios de um jogo de dados para 4 jogadores
                # guarde os resultados em um dicionaro
                # coloque o dicionarios em orgem de quem tirou o maior numero para o menor
                # mostre o conteudo do diconario
from random import randint
from time import sleep
print(f'{" Jogo Dos dados ":=^40}') 
jogadas = {}
for j in range(1,5):
    numero = randint(1,6)
    print(f'    jogador{j} tirou {numero}')
    jogadas[f'jogador{j}'] = numero
    sleep(1)

ranking = sorted(jogadas.items(), key=lambda item: item[1], reverse=True)       # isso mantem o dicionario original em sua ordem e cria uma nova lista de tuplas em ordem descrecente
                # o indice usado é porque ranking é uma lista de tupla e para cara item do indice 1 que o o valor do dados , ele organiza a ordem pedida por que se fosse indice 0 organizaria os jogadores inves dos valores
print('Ranking do jogadores:')
cont = 0
for k , v in ranking:       # do maior para o menor
    sleep(1)
    cont+=1
    print(f'    {cont}° Lugar: {k} com {v}')
print(quebra_de_linha)
print('lista de tupla >>>>>>>',ranking ,'\ndicionario >>>>>>>>>',jogadas)      # visualizaão de como ficou a lista ranking e o dicionarios

# Jeito do guanabara
print(quebra_de_linha)
print(f'{"Jeito do guanabara":-^40}')
from operator import itemgetter
print(f'{" Jogo Dos dados ":=^40}')
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
        }
ranking = list()
for k , v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1) , reverse=True)
print('Ranking do jogadores:')
for i , v in enumerate(ranking):
    print(f'{i + 1}° lugar : {v[0]}com {v[1]} ')