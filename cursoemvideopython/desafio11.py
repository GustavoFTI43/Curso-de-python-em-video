from cordes import desafio
desafio(11)
               #ler a base e altura de uma parede para calcular sua area
B = float(input(' digite a base: '))
A = float(input(' digite a altura: '))
area = (B * A )
print(f'{area} metros quadrados ')
                # calcule quantos litros de tinta e necessario para pintar essa parede
tinta = 2 # considerando 1 litro a cada 2 metros quadrados
litros = area / tinta
print (f'você ira precisar de {litros} litros para pintar esta parece')