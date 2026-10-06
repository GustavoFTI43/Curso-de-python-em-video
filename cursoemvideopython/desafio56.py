from cordes import desafio,quebra_de_linha
desafio(56)     # jeito 1
                # leia o nome,idade,sexo de 4 pessoas e mostre : a media de idade , qual nome do homen mais velho , quantas mulheres tem menor de 20 anos
lista_dados =[]
idade_media = 0     #acumulador
mulheres = 0        #contador
homen_velho = 0     #acumulador
nome_homen_velho = ''        #acumulador
for cad in range(1 ,5):     #rodando laço e recebendo os valores das variaveis
    print(f'{"_"*15}{cad}° PESSOA{"_"*15}')
    nome = str(input(f'Nome: ')).upper().strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M] ou [F]: ')).upper().strip()
    dados = {           #armazenando valores dentro do dicionario
        'nome' : nome ,
        'idade' : idade ,
        'sexo' : sexo
    }
    lista_dados.append(dados)       #armazenando dicionarios em uma lista
for cada in lista_dados:        #percorrendo itens dentro da lista de dicionario
    idade_media += cada['idade']    #acumulando valor de idade
    if cada['sexo'] == 'M':     #condição se masculino
        if homen_velho == 0 or cada['idade'] > homen_velho: # condição que verifica idade maior
            homen_velho = cada['idade']     #acumulando idade maior em variavel
            nome_homen_velho = cada['nome'] #acumulando nome em variavel
    elif cada['idade'] < 20 and cada['sexo'] == 'F': #condiçao se mulher menor 
        mulheres += 1       #contado +1 se true
media = idade_media / 4
print(f'A idade media dessas pessoas é {media}\nO homen mais velho se chama {nome_homen_velho} e tem {homen_velho} anos')
print(f'Apenas {mulheres} mulheres são menores')
print(quebra_de_linha)
desafio(56)     #jeito guanabara , mais simples
soma = 0
maioridadehomen = 0
nomehomen= ''
contmulher= 0
for p in range(1,5):
    print(f'{"-"*15}{p}°Pessoa{"_"*15}')        #O perigo oculto do in aqui: Se o usuário apertar Enter sem digitar nada (uma string vazia ""), o Python considera que o vazio está contido em qualquer string. Então "" in "M" retorna True! O programa acharia que uma pessoa sem sexo digitado é um homem.
    nome = input('Nome: ').upper().strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    soma += idade
    if sexo in 'Mmmasculino' and idade > maioridadehomen:       #fazendo com == e trocando criterio fica mais preciso a condição
        maioridadehomen = idade     
        nomehomen = nome
    if sexo in 'Fffeminino' and idade < 20:
        contmulher +=1
media = soma / 4
print(f'A média de idade dessas pessoas é {media} anos')
print(f'O homen mais velho tem {maioridadehomen} anos e se chama {nomehomen}')
print(f'Apenas {contmulher} mulheres sao menores de 20 anos')
