from cordes import desafio
desafio(107)
                # Após criar o pacote moeda
                # importe este modulo e utilize suas funçoes


from pkdesafios import moedas

p = float(input('digite um preço: R$ '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentado 10%, temos {moedas.aumentar(p,10)}')
print(f'Diminuir 13%, temos {moedas.diminuir(p,13)}')
