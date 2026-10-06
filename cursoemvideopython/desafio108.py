from cordes import desafio,quebra_de_linha
desafio(108)
                # dentro do modulo moeda
                # crie uma função para converter o valor formatado para a moeda real

from pkdesafios import moedas

p = float(input('digite um preço: R$ '))
print(f'A metade de {moedas.real(p)} é {moedas.real(moedas.metade(p))}')
print(f'O dobro de {moedas.real(p)} é {moedas.real(moedas.dobro(p))}')
print(f'Aumentado 10%, temos {moedas.real(moedas.aumentar(p,10))}')
print(f'Diminuir 13%, temos {moedas.real(moedas.diminuir(p,13))}')