from cordes import cores , desafio, quebra_de_linha
desafio(88)
                # receba um numero sendo a quantidades de jogos que sera gerado
                # sorteie 6 numeros aleatorios entre 1 e 60 e guarde numa lista
                # mostre a ou as listas(palpites de jogos)
print('-' * 74)
print(f'{"JOGA NA MEGA SENA":^78}')
print('-' * 74)
import random
from time import sleep
Q = int(input('Quantos jogos você quer que eu sorteie: ').strip())
print('-='*13,'SORTEANDO',Q, 'JOGO(S)','-='*13)
for J in range(1,Q+1):
    jogos = list()
    for n in range(0,6):
        num = random.randint(1,60)
        if num not in jogos:
            jogos.append(num)
    print(f'{cores["verde"]}Jogo {J}: {jogos}{cores["limpa"]}')
    sleep(1)
print(f'{" < BOA SORTE > ":=^74}')

# Números: 05 - 14 - 23 - 38 - 47 - 52
# Números: 11 - 22 - 34 - 40 - 49 - 56
# Números: 07 - 13 - 26 - 35 - 41 - 58

