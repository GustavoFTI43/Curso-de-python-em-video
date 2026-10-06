from cordes import desafio
desafio(7)
                # identifique o aluno e mostre sua media de aprovação/reprovação dos semestres
aluno = input('digite o nome do aluno')
semestre1 = float(input('digite a nota do primeiro semestre'))
semestre2 = float(input('digite a nota do segundo semestre'))
média = (semestre1+semestre2)/ 2
if média >= 6:
    print ('parabêns você esta aprovado!!!')
else : 
    print('Reprovado')
print ('nota média', média)