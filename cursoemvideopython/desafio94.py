from cordes import desafio , quebra_de_linha
desafio(94)
                # Leia nome , sexo e idade de varias pessoas e guarde cada uma em um dicionarios
                # guarde os dicionarios dentro de uma lista
                # mostre quantas pessoas foram cadastradas
                # mostre a media de idade do grupo
                # mostre uma lista com todas as mulheres 
                # mostre uma lista com todas pessoas com idade acima da media
cad_pessoas = list()
while True:         # Para correção de valor digitado , basta mescla uma condição com laço(while)(no caso não fiz)
    cad = dict()
    cad['Nome'] = str(input('Nome: ').strip().title())
    cad['idade'] = int(input(f'Idade de {cad["Nome"]}: ').strip())
    cad['Sexo'] = input(f'Qual o sexo de {cad["Nome"]} [M/F]: ').upper().strip()[0]
    cad_pessoas.append(cad)
    opção = input('Quer continuar? [S/N] ')[0].strip()
    if opção in 'Nn':
        break
print(quebra_de_linha)
print(f'- O grupo tem {len(cad_pessoas)} pessoas.')
soma = 0
for item in cad_pessoas:       # OBS: cada laco roda um diconario , o que evita de ter q fazer copias.
    soma += item['idade']
media = soma / len(cad_pessoas)
print(f'- A média de idade é de {media:.1f} anos.')
print('- As mulheres cadastradas foram: ', end= '')
for M in cad_pessoas:
    if M['Sexo'] in 'fF':
        print(f'{M["Nome"]}. ', end= '')
print(quebra_de_linha)
print(f'\n- Lista das pessoas que estão acima da média:')
for p in cad_pessoas:
    if p['idade'] > media:
        print(f'nome = {p["Nome"]}; sexo = {p["Sexo"]}; idade = {p["idade"]}')
    


    