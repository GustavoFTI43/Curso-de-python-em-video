                # Maior e Menor valor
from cordes import cores , desafio
desafio(65)     # soma os valores digitados , calcule a media e quantos numeros foram digitados
stop = 'S'      # imprima o maior e o menor valor e coloque uma condição para continuar o programa
cont = soma = maior = menor = 0
while stop in 'Ss':
    num = int(input('Digite um numero: '))
    cont += 1       # contando
    soma += num     # somando
    if cont == 1 :
        maior = menor = num     # Recebendo primeiro valor
    else:
        if num > maior:     # Condçoes maior/menor
            maior = num
        elif num < menor:
            menor = num
    stop = str(input('Deseja contiuar: '))[0]     # para ou continua programa
media = soma / cont
print(f'{cores["verde"]}Voce digitou {cont} numeros e a media é {media}{cores["limpa"]}')
print(f'{cores["amarelo"]}O maior valor é {maior} e o Menor {menor}{cores["limpa"]}')
                # É possivel fazer com lista tambem , mais facil




