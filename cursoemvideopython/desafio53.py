from cordes import cores,desafio,quebra_de_linha
desafio(53)     
                #leia uma frase/palavra e identifique se ela é um polidromo(inversamente identica) sem considerar espaços
frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junção = ''.join(palavras)
inverso = junção[ : : -1]       # o -1 no step faz a palavra pular de 1 em 1 ao contrario , ler invertido
print(quebra_de_linha)
print(f'a frase {junção} ao contrario é {inverso}')
if junção == inverso:
    print(f'{cores["verde"]}POLIDROMO{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}NÃO É POLIDROMO{cores["limpa"]}')