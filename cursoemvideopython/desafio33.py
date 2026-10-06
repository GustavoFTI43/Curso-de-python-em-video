from cordes import desafio
desafio(33)
                #leia 3 numeros e determine o maior e menor entre eles
a = int(input('digite o numero >> '))
b = int(input('digite outro >> '))
c = int(input('mais um >> '))
if a > b and a > c :
    print(f'{a} é o Maior')
elif a < b and a < c :
    print(f'{a} é o Menor')
else:
    False
if b > a and b > c :
    print(f'{b} é o Maior')
elif b < a and b < c :
    print(f'{b} é o Menor')
else:
    False
if c > a and c > b :
    print(f'{c} é  Maior')
elif c < a and c < b :
    print(f'{c} é o Menor')
else :
    False 