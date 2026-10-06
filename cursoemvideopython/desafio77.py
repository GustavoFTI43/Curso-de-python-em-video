from cordes import cores , desafio
desafio(77)
                # crie uma tupla com varias palavras(sem acentos)
                # mostre as vogais de cada palavra
palavras = ('APRENDER','PROGRAMAR','PYTHON','MINHA','APOSTA','CARREIRA','VIRAR','PROGRAMADOR')
for p in palavras:
    print(f'\nNa palavra {cores["amarelo"]}{p}{cores["limpa"]} as vogais sâo ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(cores['verde'],letra,cores['limpa'],end= ' ')