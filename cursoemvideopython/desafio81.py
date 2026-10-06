from cordes import cores,desafio ,quebra_de_linha
desafio(81)
                # leia varios numeros
                # mostre quantos numeros foram digitados
                # mostre a lista ordenada de forma decrescente
                # verifique e mostre se 5 foi esta na lista
lista_numeros = []
while True:
    numero = int(input('Digite um numero: '))
    lista_numeros.append(numero)
    opção = input('Quer continuar [S/N] ? ')
    if opção in "Nn":
        break
lista_numeros.sort(reverse=True)        # coloca em ordem invertida (reverse)
print(quebra_de_linha)
print(f'foram digitados {len(lista_numeros)} elementos.')
print(f'Os valores em ordem decrescente são {lista_numeros}')
if 5 in lista_numeros:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')

 






