from cordes import desafio,quebra_de_linha
desafio(87)
                # crie uma matriz
                # mostre a soma de todos os pares
                # mostre a soma dos numeros da 3° coluna
                #  mostre o maior valor da 2 linha
matriz = [
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
]
for i in range(0,3):
    for f in range(0,3):
        matriz[i][f].append(int(input(f'Digite um valor para [{i},{f}]:').strip()))
pares = soma3 = conta = maior_num = 0
print(quebra_de_linha)
for a,b,c in matriz:
    print(a,b,c)
    for a1 in a:
        if a1 % 2 == 0:
            pares += a1
    for b1 in b:
        if b1 % 2 == 0:
            pares += b1
    for c1 in c:
        soma3 += c1
        if c1 % 2 == 0:
            pares += c1
for d in matriz[1]:
    for d1 in d:
        if d1 > maior_num:
            maior_num = d1
print(quebra_de_linha)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior_num}')

                # jeito do guanabara com meu toque kkk esta mais simples porem a inha solução inicial foi a de cima 
print(quebra_de_linha)
print(f'{"jeito do guanabara":-^40}')
matriz1 = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = soma_3 = maior = 0
for a in range(0,3):
    for b in range(0,3):
        matriz1[a][b] = int(input(f'digite o valor para [{a},{b}]: ').strip())
print(quebra_de_linha)
for a in range(0,3):
    for b in range(0,3):
        print(f'[{matriz1[a][b]:^5}]',end='')
        if matriz1[a][b] % 2 == 0:
            soma_par += matriz1[a][b]
        if b == 2:
            soma_3 += matriz1[a][b]
        if a == 1:
            maior = max(matriz1[a])
    print()
print(quebra_de_linha)
print(f'A soma fos valores pares é {soma_par}')
print(f'a soma dos valores da 3° coluna é {soma_3}')
print(f'o maior numero da 2 coluna é {maior}')

