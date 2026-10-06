from cordes import desafio,quebra_de_linha
desafio(48)     
                #calcule a soma entre todos os numeros impares que são multiploes de 3 entre 1 e 500
soma = 0        #acumulador
cont = 0        #contador
for i in range(1 , 500, 2):     #loop pulando de 2 em 2 resultando nos impares
    if i % 3 == 0:      #condição de multplo de 3
        cont += 1
        soma += i
print(f'a soma de {cont} valores é de {soma}')
print(quebra_de_linha)
desafio(49)     
                #desafio 9  melhorado / leia qualquer numero e mostre sua tabuada
numero = int(input('digite um numero: '))
for n in range(1 , 11):
    r = numero * n
    print(f'{numero} X {n} = {r}')