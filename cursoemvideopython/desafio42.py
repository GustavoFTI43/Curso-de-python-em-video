from cordes import cores,desafio,quebra_de_linha
desafio(42)
                # verique se 3 valores forma 1 triangulo e indique qual triangulo se refere, semelhante ao desafio 35
while True: 
    a = float(input('digite uma metragem em cm: '))
    b = float(input('digite uma metragem em cm: '))
    c = float(input('digite uma metragem em cm: '))
    print(quebra_de_linha)
    if (a + b > c) and (a + c > b) and (b + c > a ):
        print('Com essas medidas é possivel forma um triangulo')
        if (a == b == c):
            print(f'{cores["verde"]}EQUILATER{cores["limpa"]}')
        elif (a == b) or (a == c) or (b == c):
            print(f'{cores["verde"]}ISÓSCELES{cores["limpa"]}')
        elif (a != b != c):
            print(f'{cores["verde"]}ESCALENO{cores["limpa"]}')
    else:
        print(f'{cores["vermelho"]}não foi possivel formar um triangulo{cores["limpa"]}')
    cont= input('Deseja continuar (S) ou (N): ').upper().strip()
    if cont == 'N' or cont == 'NAO' or cont == 'NÃO':
        print(f'{cores["vermelho"]}Programa encerrado{cores["limpa"]}')
        break
    print(quebra_de_linha)
