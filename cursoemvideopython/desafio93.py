from cordes import desafio , quebra_de_linha
desafio(93)
                # gerencia de aporveitamneto de jogador
                # leia nome , total de partidas do jogador
                # leia gol por cada partida e adicione tudo em um dicionario
                # guarde tambem o toal de gols
from time import sleep
aproveitamento_jogador = dict()
aproveitamento_jogador['Nome'] = str(input('Nome do jogador :').strip().title())
partidas = int(input(f'Quantas partidas {aproveitamento_jogador["Nome"]} jogou: ').strip())
aproveitamento_jogador['Gols'] = list()
for p in range(1, partidas+1):
    aproveitamento_jogador['Gols'].append(int(input(f'Quantos gol na partida {p}:')))
aproveitamento_jogador['Total'] = sum(aproveitamento_jogador['Gols'])
print(quebra_de_linha)
for k , v in aproveitamento_jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(quebra_de_linha)
sleep(1)
print(f'O jogador {aproveitamento_jogador["Nome"]} tem {partidas} partidas.')
for ind , v in enumerate(aproveitamento_jogador['Gols']):
    print(f'    => Na partida {ind + 1}, fez {v} gols.')
    sleep(0.5)
print(f'somando um total de {aproveitamento_jogador["Total"]}')
media = partidas / aproveitamento_jogador['Total']
print(quebra_de_linha)
print(f'Media de {media:.1f} gols por partida')