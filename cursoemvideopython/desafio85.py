from cordes import cores,desafio,quebra_de_linha
desafio(85)
                # leia 7 valores e cadastre em uma unica lista
                # esta lista deve estar separando os numeros pares , dos impares
                # mostre os impares e pares em ordem crescente
                
numeros = [[],[]]
for a in range(1,8):
    num = int(input(f'Digite o {a}° numero: ').strip())
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(quebra_de_linha)
print(f'{cores["verde"]}Os valores pares digitados foram: {numeros[0]}{cores["limpa"]}')
print(f'{cores["amarelo"]}Os valores impares digitados foram: {numeros[1]}{cores["limpa"]}')
