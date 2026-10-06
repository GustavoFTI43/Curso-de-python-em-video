from cordes import cores,desafio
desafio(67)
                # Mostre a tabuada de varios numeros e interrompa se for negativo
from time import sleep
while True:
    n = int(input('digite o numero para ver a tabuada (negativos sai): '))
    if n < 0 :
        break
    print('=' * 40)
    for i in range(1,11):
        R = n * i
        sleep(0.5)
        print(f'{n} X {i} = {R}')
    print('=' * 40)
print('>' * 20,'ENCERRADO','<' * 20)