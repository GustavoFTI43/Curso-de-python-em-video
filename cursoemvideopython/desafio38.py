from cordes import desafio
desafio(38)
                # compare 2 numero e veja se sao maior, menor ou iguais
num1 = int(input('digite um numero1: '))
num2 = int(input('digite um numero2: '))
if num1 > num2:
    print(f'o {num1} é maior')
elif num2 > num1:
    print(f'o {num2} é maior')
else:
    print('ambos são iguais')