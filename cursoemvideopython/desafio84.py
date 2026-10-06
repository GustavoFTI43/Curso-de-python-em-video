from cordes import cores,desafio,quebra_de_linha
desafio(84)
                # leia nome e peso de varias pessoas e guarde numa lista
                # mostre quantas pessoas foi cadastrada 
                # mostre uma lista com as pessoas mais pesada
                # mostre uma lista com as pessoas mais leves 

cad = list()
dados = list()
leve = list()
pesado = list()
totp= 0
while True:
    dados.append(input('Nome: ').strip().title())
    dados.append(int(input('Peso: ').strip()))
    cad.append(dados[:])        # Para copiar a lista dados
    dados.clear()
    totp +=1
    R = input('Quer continuar [S/N] :').upper()
    if R in 'Nn':
        break

for c , pes in enumerate(cad):
    if c == 0 :
        dados.append(pes[0])
        dados.append(pes[1])
        pesado.append(dados[:])
        leve.append(dados[:])
        dados.clear()
    elif pes[1] > pesado[0][1]:
        pesado.clear()
        dados.append(pes[0])
        dados.append(pes[1])
        pesado.append(dados[:])
        dados.clear()
    elif pes[1] == pesado[0][1]:
        dados.append(pes[0])
        dados.append(pes[1])
        pesado.append(dados[:])
        dados.clear()
    elif pes[1] < leve[0][1]:
        leve.clear()
        dados.append(pes[0])
        dados.append(pes[1])
        leve.append(dados[:])
        dados.clear()
    elif pes[1] == leve[0][1]:
        dados.append(pes[0])
        dados.append(pes[1])
        leve.append(dados[:])
        dados.clear()
    else:
        False
print(quebra_de_linha)
print(f'O maior peso foi {pesado[0][1]}. Peso de ', end= '')
for p in pesado:
    print(f'{p[0]} ...', end= '')
print(f'\n{quebra_de_linha}')
print(f'O menor peso foi {leve[0][1]}. Peso de ', end= '')
for p in leve:
    print(f'{p[0]} ...', end= '')
print(f'\n{quebra_de_linha}')
print(f'Foram cadastradas {totp} pessoas ...')
print(f'Os dados foram {cad}')

# Jeito do guanabara
# parecido , porem mais eficiente na difinição do maior e menor
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(int(input('Peso: ').strip()))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [S/N]: ').strip()[0]
    if resp in 'Nn':
        break
print(quebra_de_linha)
print(f'Ao todo foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi {mai}, Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ...' , end= '')
print(f'\nO menor peso foi de {men}, Peso de ', end='')
for p1 in princ:
    if p[1] == men:
        print(f'{[0]} ...' , end='')
