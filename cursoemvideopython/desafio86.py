from cordes import cores,desafio,quebra_de_linha
desafio(86)
                # CRIE UMA MATRIZ 3X3 E PRENCHA COM VALORES LIDOS
                # MOSTRE A MATRIZ COM A FORMATAÇÃO CORRETA
matriz = [
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
]
for i in range(0,3):
    for f in range(0,3):
        matriz[i][f].append(int(input(f'Digite um valor para [{i},{f}]:').strip()))
print(quebra_de_linha)
for a,b,c in matriz[0],matriz[1],matriz[2]:
    print(a,b,c)

print(quebra_de_linha)

# jeito do guanabara
print(f"{'jeito do guanabara':-^40}")
matriz1 = [[0,0,0],[0,0,0],[0,0,0]]
for a in range(0,3):
    for b in range(0,3):
        matriz1[a][b] = int(input(f'digite o valor para [{a},{b}]: ').strip())      # usa os 2 indices selecionados da lista
print(quebra_de_linha)
for a in range (0,3):
    for b in range(0,3):
        print(f'[{matriz1[a][b]: ^5}]', end='')
    print()


