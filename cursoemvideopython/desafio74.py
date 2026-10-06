from cordes import desafio,cores
desafio(74)
                # Gere 5 numeros aleatorios e coloque os dentro de uma tupla
from random import randint
numeros = [ ]
for i in range(5):
    a = randint(0,100)
    numeros.append(a)
tupla = (numeros)
                # mostrar listagem de numeros
print('os valores sortedos foram : ',*tupla)
                # Maior e Menor valor
print('o maior numero foi',max(tupla))
print('o menor numero foi ',min(tupla))


                # jeito do guanabara
print('=' * 40)
numeros1 = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print('os valores digitados foram: ', end= '')
for n in numeros1:
    print(f'{n}  ', end= '')
print('\no maior numero foi',max(numeros1))
print('o menor numero foi ',min(numeros1))