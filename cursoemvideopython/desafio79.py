from cordes import cores,desafio
desafio(79)
                #leia varios numeros e salve em uma lista
                # na lista nao pode ter numeros repetidos
                # mostre a lista em ordem crescente
lista = []
while True:
    numero = int(input('digite um numero: '))
    if numero not in lista:
        lista.append(numero)
        print(f'{cores["verde"]}Numero adicionado com sucesso...{cores["limpa"]}')
    else:
        print(f'{cores["amarelo"]}numero repetido nao vou adiconar ....{cores["limpa"]}')
    n = str(input('Quer continuar ? [S/N] : ')).upper().strip()
    if n == 'N':
        print(f'{cores["vermelho"]}{" ENCERRADO ":=^40}{cores["limpa"]}')
        break
lista.sort()
print('Sua lista contem este numeros >>> ',cores['amarelo'],*lista,cores['limpa'])
