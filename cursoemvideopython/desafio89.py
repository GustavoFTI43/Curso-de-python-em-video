from cordes import desafio,quebra_de_linha,cores
desafio(89)
                # leia nome e duas notas de alunos e guarde em uma lista composta
                # mostre o boletim contendo a media dessas notas
                # permita o usuario poder visualizar cada nota separadamente
import copy     # modulo para copia
alunos = [[]]           
# inves de criar duas lista vazia é possivel criar no loop outra lista para adiconar nesta lista e usar seu dados como contador
cont = 0
while True:
    alunos[cont].append(cont)
    alunos[cont].append(input('Nome: ').strip().upper())
    alunos[cont].append(float(input('Nota 1: ').strip()))
    alunos[cont].append(float(input('Nota 2: ').strip()))
    cont +=1
    cond = input('Quer Continuar?  [S/N] ')
    if cond[0] in 'Nn':
        break
    alunos.append(list())
print(quebra_de_linha)
boletim = copy.deepcopy(alunos)     # deepcopy é para copiar listas compostas e permite alterar seu items sem mecher na lista antiga
print('Na.',f'{"NOME":<14}','MÉDIA')
print('-'*30)                       # inves de fazer uma copia da lista , é possivel apenas imprimir a media 
for nota in boletim:
    media = (nota[2] + nota[3]) / 2
    nota.pop()
    nota[2] = media
    print(f'{nota[0]:<3} {nota[1]:<14} {nota[2]}')
print('-'*30)
while True:
    busca = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(alunos):
        print('ERRO , TENTE NOVAMENTE ...')
    else:
        print(f'Nota de {alunos[busca][1]} são {alunos[busca][2:]}')
    print('-'*30)
print('Finaliznado ....')
print(f'<<<< Volte Sempre >>>>')

# Jeito do guanabara , bom de fazer tambem porem a eficiencia é a mesma

print(f'{"jeito guanabara":-^45}')
ficha =list()
while True:
    nome = input('Nome: ').strip().title()
    nota1 = int(input('Nota 1:').strip())
    nota2 = int(input('Nota 2: ').strip())
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    resp = input('Quer continuar?[S/N] ')[0].strip().upper()
    if resp in 'Nn':
        break
print(quebra_de_linha)
print('Na.',f'{"NOME":<14}','MÉDIA')
print('-'*30)
for i , v in enumerate(ficha):
    print(f'{i:<4}{v[0]:<15}{v[2]:<8.1f}')
while True:
    busca = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(ficha):
        print('ERRO , TENTE NOVAMENTE ...')
    else:
        print(f'Nota de {ficha[busca][0]} são {ficha[busca][1]}')
    print('-'*30)
print('Finaliznado ....')
print(f'<<<< Volte Sempre >>>>')

    










