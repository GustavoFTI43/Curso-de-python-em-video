from cordes import desafio,quebra_de_linha,cores
desafio(101)
                # crie uma função chamada voto que recebera o ano de nascimento como parametro
                # ela retornara um valor literal que idica se o voto sera (negado , opcional , obrigatório)
def voto(ano_nascimento):
    '''
    recebe ano de nascimento
    importa modulo para ano atual
    verifica idade da pessoa
    veriricacondiçao de voto para:
    < 16 : nao vota
    16 a 18 opcional
    > 18 obrigatório
    '''
    from datetime import datetime
    ano_atual = datetime.now().year
    idade_da_pessoa = ano_atual - ano_nascimento
    if idade_da_pessoa >= 16 and idade_da_pessoa < 18 or idade_da_pessoa > 70:
        return f'Com {idade_da_pessoa} : Voto opcinal'
    elif idade_da_pessoa < 16 :
        return 'Menor de 16 : Voto negado'
    else:
        return f'Com {idade_da_pessoa} : Voto obrigatório'

print(quebra_de_linha)
ano = int(input('Digite o ano de nascimento:'))
restultado = voto(ano)
print(restultado)



