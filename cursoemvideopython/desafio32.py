from cordes import desafio
desafio(32)
                # ler um ano qualquer e indicar se é bissexto ou nao
ano = int(input('digite um ano qualquer'))      # leitura do ano
import calendar     #importando modulo
anoBI = calendar.isleap(ano)     # metodo que retorna true se for ano bissexto
if anoBI == True:
    print(f'este ano de {ano} é bissexto')
else:
    print(f'{ano} não é bissexto') 