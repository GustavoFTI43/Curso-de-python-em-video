from cordes import desafio
desafio(37)
                #Leia um numero inteiro e mude a base de conversão
numero = int(input('digite um numero: '))
base = int(input('digite o numero da convesão\n(1) Binario \n(2) Octonal\n(3) Hexadecimal\n>>>>> '))
if base == 1:
    print(f'{numero:b} ou', end=" " )       #f-string
    print(bin(numero)[2:],'em função bin')      #função bin

elif base == 2:
    print(f'{numero:o} ou', end=' ')
    print(oct(numero)[2:],'em função oct')      #função oct
elif base == 3:
    print(f'{numero:x} ou', end=' ')
    print(hex(numero)[2:],'em função hex')      #função hex
else:
    print('erro')