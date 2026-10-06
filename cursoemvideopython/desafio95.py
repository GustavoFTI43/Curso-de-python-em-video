from cordes import desafio,quebra_de_linha,cores
desafio(95)
                # aprimoramento do desafio 93
                # cadatras varios jogadores e ver seus aproveitamentos
lista_jogadores = list()
while True:
    jogador = dict()
    jogador['nome']= input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou: ').strip())
    jogador['gols'] = list()
    if partidas == 0:
        jogador['gols'] = ''
        jogador['total'] = 0
    else:
        for p in range(1,partidas+1):
            jogador['gols'].append(int(input(f'Quantos gols na partida {p}: ')))
        jogador['total'] = sum(jogador['gols'])
    print(len(jogador['gols']))
    lista_jogadores.append(jogador)
    opção = input('Quer continuar? [S/N] ').strip()[0].upper()
    if opção in 'Nn':
        break
print(quebra_de_linha)
print('cod', f'{"Nome":<14}',f'{"Gols":<14}','Total')
print('-' * 40)
for i , v in enumerate(lista_jogadores):
    gol_txt = str(v['gols'])
    if gol_txt == '':
        gol_txt = '0'
    print(f'{i:<3} {v["nome"]:<14} {gol_txt:<14}{v["total"]}')
print('-' * 40)
dados_jogador = 0
while True:
    dados_jogador = int(input('Mostrar dados de qual jogador: [999 para sair] ').strip())
    print('-' * 40)
    if dados_jogador == 999:
        print(f'{cores["vermelho"]}Encerrando ....{cores["limpa"]}')
        break
    elif dados_jogador >= len(lista_jogadores) or dados_jogador < 0:
        print(f'{cores["amarelo"]}jogador não encontrado tente denovo...{cores["limpa"]}')
    else:
        v = lista_jogadores[dados_jogador]      # inves de rodar um laco e conta os indice ate chegar no certo
                                                # guarde o dicionario que precisa em uma variavel e rode seus itens normalmente isso simplificara o codigo
        print(f'{cores["verde"]}-- Levantamento do jogador {v["nome"]}{cores["limpa"]}')
        if len(v['gols']) == 0:
            print('     Não jogou nenhuma partida')
        else:
            for c , gols in enumerate(v['gols']):
                print(f'    No {c + 1}º jogo fez {gols} gols')
print(quebra_de_linha)
print(f'{cores["vermelho"]}>>>>>>Programa Enceradoo<<<<<<{cores["limpa"]}')


            
        


        
