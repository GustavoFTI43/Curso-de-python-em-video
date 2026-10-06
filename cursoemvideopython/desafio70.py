                # leia o nome e preço de varios produtos , com oção de parada
                # mostre o total gasto com os produtos , quantos excede o valor de 1000 reais e qual nome do mais barato
from cordes import cores,desafio
desafio(70)
print('-='*40,'\n       LOJA VEMQUITEM')
print('-='*40)
soma = maior_mil = cont = menor_preço= 0
produto_barato = ''
while True:
    nome = input('nome do produto:')
    preço = float(input('digite o preço: '))
    soma += preço
    cont += 1
    if cont == 1 or preço < menor_preço:
        menor_preço = preço
        produto_barato = nome
    if preço > 1000:
        maior_mil +=1
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N] : ')[0].upper().strip()
    if resp == 'N':
        print(f'{cores["vermelho"]}{" FIM DO PROGRAMA ":=^40}{cores["limpa"]}')     # texto formatado
        break
print(f'>>>> Voce gastou um total de {soma:,.2f} R$')       # Depois da virgula apenas 2 casas para decimais
print(f'>>>> {maior_mil} produtos excedeu o valor de 1000 R$')
print(f'>>>> O produto mais barato foi {produto_barato} e custou {menor_preço:,.2f} R$')        # Depois da virgula apenas 2 casas para decimais
