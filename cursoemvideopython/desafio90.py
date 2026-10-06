from cordes import desafio
desafio(90)
                # Leia o nome e a media de um aluno e a situação de aprovação
                # guarde tudo dentro de um dicionarios
                # mostre o conteudo que esta dentro do diconario
nome = input('Digite seu nome: ').strip().title()
media = float(input(f'Digite a media de {nome}: ').strip())
if media > 6.5 :
    resultado =  'aprovado(a)'
else:
    resultado = 'reprovado(a)'
aluno = dict()
aluno['nome'] = nome
aluno['media'] = media
aluno['situação'] = resultado
for k , v in aluno.items():
    print(f'{k} é igual a {v}')