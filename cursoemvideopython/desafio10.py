from cordes import desafio
desafio(10)
              # ler um valor em real e mostrar quantos dolares da para comprar
real = float(input('digite quanto dinheiro você tem: '))
dolar = float( real / 5.00 )
if real >= 5.00:
    print (f'voce pode ter {dolar:.2f} dolares')
else :
    print(f' este valor de {real} reais não é suficiente para comprar dolar')