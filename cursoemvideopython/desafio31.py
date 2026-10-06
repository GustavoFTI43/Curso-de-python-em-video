from cordes import desafio
desafio(31)
                # verificar distancia de viagem por km e mostrar valor das passagens , ate 200km 0,5RS por KM , acima de 200km 0,45RS
distancia = int(input('distancia da viagem')) # lendo distancia
if distancia <= 200 : # aplicação de condição na distancia 
    a = float(0.5 * distancia) # calculo de passagem 
    print(f'Sua viagem custara {a} R$')
else:
    b = float(0.45 * distancia)
    print(f'viagem com mais de 200km de distancia(desconto de 10%)\nSua viagem custara {b} R$') 
