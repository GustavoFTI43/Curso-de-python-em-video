from cordes import cores,desafio,quebra_de_linha
desafio(80)
                # leia 5 numeros digitados 
                # organize os numeros dentro da lista sem usar sorted ou sort
                # mostre a lista organizada
lista = []
for i in range(5):
    numero = int(input('digite um valor: '))
    if i == 0 or numero >= lista[-1]:
        lista.append(numero)
        print('adiconando ao final da lista....')
    elif numero < lista[0]:
        lista.insert(0,numero)
        print('adicionando na posição 0 da lista')
    elif numero > lista[0] and numero < lista[1]:
        lista.insert(1,numero)
        print('adicionando na posição 1 da lista')
    elif numero > lista[1] and numero < lista[2]:
        lista.insert(2,numero)
        print('adicionando na posição 2 da lista')
    elif numero > lista[2] and numero < lista[3]:
        lista.insert(3,numero)
        print('adicionando na posição 3 da lista')
print(quebra_de_linha)
print(f'Os valores digitados em ordem foram {cores["amarelo"]}',*lista,cores["limpa"])
                # Jeito do guanabara
print(f'{"jeito guanabara":-^40}')
lista1 = []
for a in range (0,5):
    num = int(input('Digite um valor'))
    if a == 0 or num > lista1[-1]:
        lista1.append(num)
        print('Adicionando ao final da lista ...')
    else:
        pos = 0     # contador
        while pos < len(lista1):
            if num < lista1[pos]:
                lista1.insert(pos, num)
                print(f'Adicionando na posição {pos} da lista ...')
                break
            pos += 1
print(quebra_de_linha)
print(f'os valores digitados em orfem foram',*lista1)
