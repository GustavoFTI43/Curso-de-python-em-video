from cordes import desafio
desafio(22) 
                #criar programa que le o nome completo de uma pessoa 
nome= str(input('digite seu nome completo: '))
print(nome.upper())     # mostre o nome com todas as letrar maiusculas
print(nome.lower())     # mostre com todas letrar minusculas
nomesem = nome.replace(' ','')      # mostrar quantas letras tem no nome sem considerar espaços
print('este nome possui ',len(nomesem),' letras')
nomep = nome.split()        # mostre quantas letras tem o primeiro nome 
print ('seu primeiro nome tem ',len(nomep[0]),' letras')