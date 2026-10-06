from cordes import desafio , quebra_de_linha
desafio(109)
                # modifique as funçoes criadas no modulo (moedas)
                #criando um parametro que infoma se o valor vai ser formatado ou nao pela funçao real
from pkdesafios import moedas
p = float(input('digite um preço: R$ '))
print(f'A metade de {moedas.real(p)} é {moedas.metade(p , True)}')
print(f'O dobro de {moedas.real(p)} é {moedas.dobro(p , True)}')
print(f'Aumentado 10%, temos {moedas.aumentar(p , 10 , True)}')
print(f'Diminuir 13%, temos {moedas.diminuir(p , 13 , True)}')