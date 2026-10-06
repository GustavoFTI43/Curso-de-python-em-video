from cordes import cores,desafio
desafio(75)
                # leia 4 valores digitados e guarde em uma tupla
n1 = int(input('digite o 1° numero: '))
n2 = int(input('digite 0 2° numero: '))
n3 = int(input('digite o 3° numero: '))
n4 = int(input('digite o 4° numero: '))
numeros = (n1 , n2 , n3 , n4)       # Voce pode colocar para entrar(input) direto na tupla
# exemplo numeros = ((int(input(digite o 1° numero)),(int(input(digite o 2° numero)))
print('=' * 40)
                # Mostre os numeros digitados
print(f'Voce digitou os numeros : {numeros}')
                # Mostre quantas vezes o 9 apareceu
if 9 in numeros:
    print(f'O numero 9 apareceu {numeros.count(9)} vezes')
else:
    print('O 9 nao foi digitado')
                # mostre em qual posição o numero 3 aparece
if 3 in numeros:
    print(f'O numero 3 aparece na {numeros.index(3)+1}° posição')
else:
    print('O 3 nao foi digitado.')
                # Mostre quais numeros digitados é par
print(f'Os valores pares digitados que sao ', end= '')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} ', end= '')
