from cordes import desafio,quebra_de_linha
                #Estrutura de repetição while
desafio(57)     #leia o sexo masculino e feminino de uma pessoa , e se o valor digitado for diferente , peca para corrigir
nome = input('what your name: ')
sexo = str(input('What is your sex? [M/F]: ')).upper().strip()
print(quebra_de_linha)
while sexo[0] not in 'MF':
    sexo = str(input('resposta invalida tente novamente? [M/F]: ')).upper().strip()
print(f'Sexo {sexo} registado com sucesso')