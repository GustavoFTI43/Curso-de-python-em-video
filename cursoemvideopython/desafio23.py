from cordes import desafio
desafio(23)
                # leia um numero de 0 a 9999 e mostre ele separado por unidade
numero = int(input('digite de 0 a 9999: '))
                # usando matematica para difinir unidades , dezena , cnetena e milhar
                # pode usar str tambem porem não da exatamente certo
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('unidade:', u ,'\ndezena:', d ,'\ncentena:', c ,'\nmilhar:', m)