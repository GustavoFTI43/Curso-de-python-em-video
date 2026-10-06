from cordes import desafio
desafio(15)
                 # calcule o valor a pagar de um carro alugano baseado nos dias (60Rs o dia) e km rodado (0.15 por km)
                # valor diario 
car = int(input('digite quantos dias'))
                # kilometragem 
km = float(input('digite quanto voce rodou'))
aluguel = car * 60 + km * 0.15
print (f'o aluguel do carro saiu a {aluguel}')