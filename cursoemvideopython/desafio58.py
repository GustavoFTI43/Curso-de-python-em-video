from cordes import desafio
desafio(58)
                #melhore o desafio 28 , tente adivinhar o numero escolhido pelo computador , e conte quantas vezes vc chutou ate acerta
import random
chute = 0
numero = random.choice(range(1,10))
seu_numero = 0
while seu_numero != numero:
    seu_numero = int(input('qual numero de 1 a 10 o computador sorteio ?\n'))
    chute +=1
print(f'voce tentou umas {chute} vezes antes de acerta o numero\nnumero sorteado {numero}')
