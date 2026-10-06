from cordes import desafio,cores
desafio(72)
                # crie uma tupla de 0 a 20 por extenso
                # leia o numero do usuario e mostre o valor por extenso
numeros = ('Zero','Um','Dois','Três','Quatro','Cinco',
           'Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Quatorze','Quinze',
           'Dezeseis','Dezesete','Dezoito','Dezenove','Vinte')
while True:
    n = (int(input('Digite um numero entre 0 e 20: ')))
    if n >= len(numeros) or n < 0:
        print('tente novamente. ', end= '')
    else:
        break
print(f'Voce digitou o numero {cores["verde"]}{numeros[n]}{cores["limpa"]}')
