from cordes import cores,desafio,quebra_de_linha
desafio(39)
                # leia a data de nascimento e verifique se é ano de alistamneto ou se ainda vai se alistar
from datetime import datetime       # modulo de data
nsc = int(input('digite o seu ano de nacimento: ').strip())
ano_atual = datetime.now().year     #.now com datatime , veririca a data e hora atual do computador 
idade = ano_atual - nsc
                #condiçoes para alistamento
print(quebra_de_linha)
if idade == 18:
    print(f'{cores["verde"]}você tem {idade} anos e ja pode fazer seu alistamento ainda este ano!!!{cores["limpa"]}')
elif idade < 18:
    saldo = 18 - idade
    ano = ano_atual + saldo
    print(f'Você ainda tem {idade} anos e só podera se alistar em {ano}')
elif idade > 18 :
    saldo = idade - 18
    ano = ano_atual - saldo
    print(f'Você tem {idade} anos e deveria ter se alistado em {ano}')
else:
    False
