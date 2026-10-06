from cordes import cores,desafio,quebra_de_linha
desafio(52)
                #digite um numero é verifique se ele é numero primo
numero = int(input('digite um numero: '))
valido = 0      #contador
if numero <2:   #condição de numeros primos tem q ser acima de 2
    print('numero invalido')
else:
    for p in range(1,numero+1): #laço,loop in sequencia de 1 a valor da variavel
        if numero % p == 0:
            print(f'{cores["verde"]}{p}{cores["limpa"]}',end= ' ')      # verde é primo
            valido += 1     #contagem de quantas vezes foi valido a conição no loop
        else:
            print(f'{cores["vermelho"]}{p}{cores["limpa"]}',end= ' ')       # vermelho não é primo
    print(f'\n{quebra_de_linha}')
    print(f'O numero {numero} foi divisivel {valido} vezes', end=' ')
    if valido == 2:     #contador usado para validar numero primo
        print(f'e é {cores["verde"]}PRIMO{cores["limpa"]}')
    else:
        print(f'e não é {cores["vermelho"]}PRIMO{cores["limpa"]}')