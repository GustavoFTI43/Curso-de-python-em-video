from cordes import cores,desafio
desafio(41)
                # clasifique os atletas de acordo com a idade
from datetime import date
ano_nsc = int(input('Ano De Nascimento: '))
atual = date.today().year # verifica a data 
idade = atual - ano_nsc
if idade <= 9 :
    print(f'Você é um atleta de {idade} anos\n {cores["verde"]}CLASSIFICAÇÃO : MIRIM {cores["limpa"]}')
elif idade > 9 and idade <= 14:
    print(f'Você é um atleta de {idade} anos\n {cores["verde"]}CLASSIFICAÇÃO : INFANTIL {cores["limpa"]}')
elif idade > 14 and idade <= 19:
    print(f'Você é um atleta de {idade} anos\n {cores["verde"]}CLASSIFICAÇÃO : JUNIOR {cores["limpa"]}')
elif idade > 19 and idade <= 25:
    print(f'Você é um atleta de {idade} anos\n {cores["verde"]}CLASSIFICAÇÃO : SENIOR {cores["limpa"]}')
else:
    print(f'Você é um atleta de {idade} anos\n {cores["verde"]}CLASSIFICAÇÃO : MASTER {cores["limpa"]}')
