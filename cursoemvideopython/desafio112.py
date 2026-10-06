from cordes import desafio
desafio(112)
                #dentro do pacote pkdesafios crie um modulo chamado dados()
                #neste modulo crie a função leiadinheiro
                # que trabalhara como o input , mas para validação de dados numericos
                # so pode receber numeros sendo eles com vigura ou com ponto(valores monetarios)
                # depois no desafio retorne  essa função junto com a resumo do modulo moedas
from pkdesafios import moedas, dados
p = dados.leiadinheiro('digite um preço: R$')
moedas.resumo(p , 10 , 15)