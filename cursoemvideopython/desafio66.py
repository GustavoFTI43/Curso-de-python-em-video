from cordes import cores,desafio
desafio(66)
                # tratado varios numeros  flag
cont = soma = 0
while True:
    n = int(input('digite um numero: (999 para parar) >> '))
    if n ==  999:
        break
    cont +=1
    soma += n
print(f'{cores["amarelo"]}Voce digitou {cont} numeros , a soma deles é {soma}{cores["limpa"]}')

