from cordes import desafio
desafio(54)
                #leia o ano de nacimento de 7 pessoas e mostre quantas são de maiores
from datetime import datetime
ano = datetime.now().year       # coleta apenas o ano atual
maiores_cont = 0
menores_cont = 0
for i in range(1, 8):
    nascimento = int(input(f'digite o ano em que a {i}° pessoa nasceu: '))
    de_maior = ano - nascimento
    if de_maior >= 18:
        maiores_cont += 1
    else :
        menores_cont +=1
print(f'Das 7 pessoas {maiores_cont} são maiores e {menores_cont} são menores de idade!!!')
