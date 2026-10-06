from cordes import desafio , quebra_de_linha
desafio(92)
                # Leia nome, ano de nascimento e carteira de trabalho(ctps)
                # cadastre em um dicionario
                # se ctps for diferente de 0 receba ano de contratação e salario
                # calcule e acrscente alem da idade , o que a pessoa vai se aposentar
from datetime import datetime
ano_atual = datetime.now().year
cad = dict()
cad['Nome'] = input('Nome completo: ').title().strip()
ano_nascimento = int(input('Ano que nasceu: ').strip())
cad['Idade'] = ano_atual - ano_nascimento
cad['CTPS'] = int(input('Carteira de trabalho (0 nao possui): ').strip())
if cad['CTPS'] != 0:
    cad['Ano de Contratação'] = int(input('Ano de Contratação: ').strip())
    cad['Salario'] = int(input('Salario: ').strip())
    cad['Aposentadoria'] = (cad['Ano de Contratação'] - ano_nascimento) + 35
print(quebra_de_linha)
for k , v in cad.items():
    print(f'- {k} tem o valor: {v}')
print('voce é menor de 16 ainda' if cad["Idade"] < 16 else '')