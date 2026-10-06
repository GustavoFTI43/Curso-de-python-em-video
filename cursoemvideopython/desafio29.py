from cordes import desafio
desafio(29)
                 # ler a velocidade de um carro e se ele ultrapassar 80 km imprima notificação e uma multa de 7 reais por km
km_hora = int(input('kilometragem por hora do veiculo >> '))        # lendo velocidade
total = 7 * km_hora
if km_hora > 80 :       # verificando se passou da condição de km/h
    print('oh ouh , você foi multado !!!')
    print(f'a multa é de 7 reais por km\ntotal multa: {total}R$')
else: 
    print('livre de multa hoje') 