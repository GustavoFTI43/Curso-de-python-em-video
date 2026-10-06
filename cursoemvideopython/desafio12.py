from cordes import desafio
desafio(12)
                # leia o preco de um produto e aplique 5% de desconto
p= float(input('preço do produto: '))
descoto = p * 0.05
pfinal= p - descoto
print (f'o valor com desconto adicionado é de R${pfinal}')