def calculo_imc(p, a):
    imc = p / (a ** 2)
    print (f'Seu imc é {imc :.3f}')
    if imc >= 18.5 and imc <= 24.9:
        print (f'{cores["verde"]}Parabéns !!! você esta no peso ideal.{cores["limpa"]}')
    elif imc < 18.8:
        print(f'{cores["vermelho"]}Você esta abaixo do peso.{cores["limpa"]}')
    elif imc >= 25 and imc <= 29.9:
        print(f'{cores["vermelho"]}você esta acima do peso.{cores["limpa"]}')
    elif imc >= 30 and imc <= 34.9:
        print(f'{cores["vermelho"]}Atenção, você atingiu o 1º grau de obesidade.{cores["limpa"]}')
    elif imc >= 35 and imc <= 39.9:
        print(f'{cores["vermelho"]}Atenção, você atingiu o 2º grau de obesidade.{cores["limpa"]}')
    elif imc > 40:
        print(f'{cores["vermelho"]}Atenção,você atingiu o 3º grau de obesidade.{cores["limpa"]}')
    else: 
        print('erro')
from cordes import cores,desafio,quebra_de_linha
desafio(43)
                # imprima uma saudação ao usuario
nome = input ('digite seu nome: ')
print(f'{cores["subazul"]}seja bem vindo {nome}! vamos consulta seu imc{cores["limpa"]}')
                # recolha as informacoes de peso e altura 
idade = input ('quantos anos você tem ')
peso = float(input('qual seu peso '))
altura = float(input('quantos voce tem de altura '))
print(quebra_de_linha)
calculo_imc(peso, altura)
                # fiz por conta porem caiu no desafio tambem