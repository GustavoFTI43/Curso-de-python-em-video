from cordes import cores , desafio,quebra_de_linha
desafio(82)
                # leia varios numeros e coloque em uma lista
                # crie 2 listar extras sendo para numeros par e impar
                # mostre as 3 listas
numeros = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = input('Quer continuar [S/N] ? ')
    if r in 'Nn':
        break
print(quebra_de_linha)
print('A lista completa é', *numeros)
print('A lista de pares é', *par)
print('A lista de impares é', *impar)