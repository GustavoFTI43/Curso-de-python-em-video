from cordes import cores , desafio,quebra_de_linha
desafio(78)
                # leia 5 valores e guarde em uma lista
                # mostre qual o maior e o menor numero e suas posicoes
numeros = []
for i in range(1,6):
    numeros.append(int(input(f'digite o {i}° valor: ')))
print(quebra_de_linha)
print('Voce digitou os valores ',cores['verde'],*numeros,cores['limpa'])     # A ESTRELA (*) MOSTRA LISTA SEM COLCHETE E SE COLOCAAR sep=',' coloca virgula entre as string se for o caso
print(f'O maior numero foi {max(numeros)} na posição ', end= '')
for c , v in enumerate(numeros):        # c é o indice da lista , enumerate mostra chave e valor da lista , no caso chave(indice)
    if v == max(numeros):
        print(f'{c} ... ' , end= '')
print(f'\nO menor numero foi {min(numeros)} na posição ', end= '')
for c , v in enumerate(numeros):
    if v == min(numeros):
        print(f'{c} ... ', end= '')
        

   