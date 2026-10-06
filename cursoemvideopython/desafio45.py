from cordes import cores,desafio,quebra_de_linha
desafio(43)
print(f'{" JOGO DO JO KEN PO ":=^74}')
import time
import random       # modulo de sorteio de numeros
while True:         # loop para rodar toda hora
    try:            # corrigir erro valor.    OBS: conhecendo este metodo mais não mostrou no curso ainda 
                    # dicionario com opçoes
        opção = {
        1 : 'PEDRA' ,
        2 : 'PAPEL' ,
        3 : 'TESOURA'
        }
                    #lendo opçao do jogador
        eu = int(input('(1) PEDRA\n(2) PAPEL\n(3) TESOURA\n(0) SAIR\nSELECIONE UMA OPÇÃO: '))
                    #condiçao para encerrar loop 
        if eu == 0 :
            print(f'{cores["verde"]}OBRIGADO POR JOGAR!!!{cores["limpa"]}')
            break
                    #condição se opção nao existe
        if eu not in opção:
            print(f'{cores["vermelho"]}OPÇÃO INVALIDA, TENTE DENOVO ...{cores["limpa"]}')
            continue

        jogo = opção[eu]
                    # sorteie um valor dentro de opçoes e coloque na maquina 
        maquina = random.choice(list(opção.values())) 
        print(quebra_de_linha)
        print(' JO')
        time.sleep(1)
        print('         KEN')
        time.sleep(1)
        print('                         PO')
                    # codição de vitoria se nao derrota
        print(quebra_de_linha)
        if jogo == maquina:
            print(f'{cores["preta"]}EMPATOU!!!{cores["limpa"]}')
        elif (jogo == 'PEDRA') and (maquina == 'TESOURA') or \
        (jogo == 'PAPEL') and (maquina == 'PEDRA') or \
        (jogo == 'TESOURA') and (maquina == 'PAPEL'):
            print(f'{cores["verde"]}JOGADOR VENCEU, {jogo} VENCE {maquina}!!!{cores["limpa"]}')
        else:
            print(f'{cores["vermelho"]}MAQUINA VENCEU, {maquina} VENCE {jogo}!!!{cores["limpa"]}')
        print(f'JOGADOR JOGOU : {jogo}\nMAQUINA JOGOU : {maquina}')
        print(quebra_de_linha)
        time.sleep(5)
    except ValueError:
        print(f'{cores["vermelho"]}ERRO,DIGITE APENAS NUMEROS{cores["limpa"]}')
