from cordes import desafio,cores,quebra_de_linha
desafio(60)
                # leia um numero e mostre seu valor fatorial faça com for e while tambem
import math
stop = ''
while stop != 'encerrar':
    numero1 = int(input('digite um  numero ou 00 para sair: '))
    fatorial = math.factorial(numero1)
    if numero1 == 0:
        stop = 'encerrar'
    elif numero1 == 1 :
        print(f'{cores["amarelo"]}NA EQUAÇÃO FATORIAL 0 E 1 SEMPRE É 1.{cores["limpa"]}')
    else:
        print(f'Calculando {numero1}! = ', end='')
        for n in range(numero1, 0, -1):
            if n == 1:
                print(n , end='')
            else:
                print(f'{n} x ', end='')
        print(' = ', fatorial)
print('programa encerrado')
print(quebra_de_linha)
                # jeito guanabara esta melhor
                # sem utilzar biblioteca math
n2 = int(input('Digite um numero:'))
fac2 = 1
cont = n2
print(f'Calculando {n2}! = ', end=' ')
while cont > 0:
    print(cont , end=' ')
    print('x' if cont > 1 else '=' , end= ' ')
    fac2 *= cont
    cont -= 1
print(fac2)
print(quebra_de_linha)
                # fazendo com for
n3 = int(input('Digite um numero: '))
fac3 = 1        # ou use o modulo
print(f'Calculando {n3}! =' , end=' ')
for n in range(n3 ,  0 , -1):
    fac3 *= n
    print(n , end=' ')
    print('x' if n > 1 else '=' , end=' ')
print(fac3)
    





    