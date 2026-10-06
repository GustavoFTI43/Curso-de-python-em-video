from cordes import cores,desafio
               # 19, Sortear 1 aluno entre os 4 digitados
                # 20 Sortear a ordem de apresentação de trabalho escolar 

desafio(19) , desafio(20)
import random
print ('Digite 4 nomes')
a = input(' 1 ')
b = input(' 2 ')
c = input(' 3 ')
d = input(' 4 ')
alunos = [a, b, c, d ]
random.shuffle(alunos) #embaralhar a ordem da lista
S = random.choice(alunos) # sortear 1 aluno 
print(f'aluno sorteado: {S} \nordem de apresentação>>> {alunos}')
                # O exercicio 21 mp3 tinha que baixar modulo entao não inclui ele aqui porem foi feito
    