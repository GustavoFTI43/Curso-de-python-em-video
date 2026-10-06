from cordes import desafio,quebra_de_linha
                # crie uma função chamada ficha
                # e receba 2 parametros opcionais (nome jogador , gols marcados)
                # mostre a ficha do jogador mesmo que um dado seja digitado errado
def ficha1(nome = '<Desconhecido>', gols = '0'):
    if nome in '0123456789' or nome == '':
        nome = '<Desconhecido>'
    if gols == '' or gols not in '0123456789':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome_jogador = str(input('Nome do jogador:')).strip().title()
gol_marcados = input('Numero de gols:')
ficha1(nome_jogador , gol_marcados)

# jeito guanabara

def ficha(nome = '<Desconhecido>' , gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

print(quebra_de_linha)
nome_jogador = str(input('Nome do jogador:')).strip().title()
gol_marcados = input('Numero de gols:')
if gol_marcados.isnumeric():
    gol_marcados = int(gol_marcados)
else:
    gol_marcados = 0
if nome_jogador == '':
    ficha(gols = gol_marcados)
else:
    ficha(nome_jogador,gol_marcados)