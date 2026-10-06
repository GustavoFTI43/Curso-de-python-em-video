from cordes import desafio
desafio(26)
                # programa que le quantos 'A' tem numa frase, mostre onde esta o primeiro 'A'  e o ultimo
frase =  input('digite uma frase: ').lower().strip()
print('esta frase tem' , frase.count('a'), 'letras (a)')     # quantidade de letra 'a' que tem na frase
print('a primeira letra (a) aparece na posição ',frase.find('a'))  # qual a posição do primeiro 'a'
print('a ultima letra (a) aparece na posição ',frase.rfind('a'))   # qual a posiçao do ultimo 'a' 