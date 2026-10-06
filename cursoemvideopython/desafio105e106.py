from cordes import desafio,quebra_de_linha
desafio(105)
                #

def notas(*n , sit = False):
    ''''
    => função para analizar notas e situação de aluno.
    n para : uma ou mais notas (recebe multiplos parametros)
    sit para : valor opcional , indica a situação do aluno
    return : retorna dicionario com varias informaçoes sobre o aluno
    '''
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor']= min(n)
    soma = 0
    for notas in n:
        soma += notas
    media = soma / len(n)
    aluno['media'] = media
    if sit == True:
        if aluno['media'] < 6 :
            aluno['situação'] = 'RUIM'
        elif aluno['media'] >= 6 and aluno['media'] <= 8:
            aluno['situação'] = 'RAZOAVEL'
        elif aluno['media'] > 7:
            aluno['situação'] = 'BOA'
        return aluno
    else:
        return aluno

resp = notas(9,0,10,9, sit= True)
help(notas)
print(quebra_de_linha)
print(resp)
    
        

