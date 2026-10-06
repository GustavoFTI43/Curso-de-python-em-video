                # Tratando Varios numeros
from cordes import cores , desafio
desafio(64)
num = cont = soma = 0
while num != 999 :
    num = int(input('Digite um numero [999 para encerrar]: '))
    if num != 999 :
        cont += 1
        soma += num
print(f'{cores["verde"]}Voce digitou {cont} numeros e a soma deles é {soma}{cores["limpa"]}')

