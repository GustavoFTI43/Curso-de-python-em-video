from cordes import cores, desafio,quebra_de_linha
desafio(76)
                # em uma unica tupla , coloque o produto e preço na sequencia
                #mostre a listagem de preço , organizando os dados de forma tubular
produto_preço = ('lapis',3.50,'caneta',7,'borracha',5,'apontador',5,'caderno',12)
print(f'-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print(f'-' * 40)
for item in produto_preço:
    if type(item) is str:
        print(f'{cores["verde"]}{item:.<40}', end= '')
    else:
        print(f' R$ {item:.2f}{cores["limpa"]}')
print(f'-' * 40)
print(quebra_de_linha)
                # jeito do guanabara

print(f'{"jeito guanabara":-^40}')
for i in range(0,len(produto_preço)):       # len devolve a quantidade de indice dentro da tupla
    if i % 2 == 0:
        print(f'{produto_preço[i]:.<40}', end='')
    else:
        print(f'R$ {produto_preço[i]:.2f}')


