                # JOGO DE IMPAR OU PAR
import random
from cordes import cores,desafio
from time import sleep
desafio(68)
cont = 0
print('-=' * 40,'\nVAMOS JOGAR IMPAR OU PAR')
while True:
    print('-=' * 40)
    pc = random.randint(1,10)       # Sorteira numeros entre colchete
    num = int(input('Digite um valor >>> '))
    opção = input('Impar ou Par [I/P] >>> ')[0].upper().strip()     #valor de variavel digitada só recebe primeira letra
    soma = pc + num
    if soma % 2 == 0:       #condição para impar ou par
        impar_par = 'PAR'
    else :
        impar_par = 'IMPAR'
    print('-' * 40)
    print(f'Voce jogou {num} e o computador {pc}.Total {soma} deu {impar_par}')
    sleep(1.5)
    if opção == impar_par[0]:       #Condição de vitoria
        print(f'{cores["verde"]}VOCE VENCEU!!!{cores["limpa"]}\nVamos Jogar novamente...')
        cont +=1
    else:
        print(f'{cores["vermelho"]}VOCE PERDEU{cores["limpa"]}')
        break
print('-' * 40)
print(f'{cores["amarelo"]}Voce venceu {cont} rodadas.\n GAME OVER {cores["limpa"]}')
    

    

