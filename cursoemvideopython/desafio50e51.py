from cordes import desafio,quebra_de_linha
desafio(50)
                # numeros pares soma , impares desconsidere
soma = 0
cont = 0
for i in range(6):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        cont +=1
        soma += num
print(f'a soma dos {cont} numeros pares é {soma}')
print(quebra_de_linha)
desafio(51)
                # progressao aritimetica , leia o primeiro termo e a razão e mostre os 10 primeiros termos desta P.A
termo = int(input('digite um numero: '))
razao = int(input('digite a razão dentre os numeros: '))
for i in range(10):
    if i == 0:
        print(f'{termo} ', end= '')
    else:
        termo+= razao
        print(f'{termo} ', end= '')