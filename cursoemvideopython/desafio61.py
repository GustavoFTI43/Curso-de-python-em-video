from cordes import cores,desafio
desafio(61)
                # Progressao Aritmetica com while mostrando os 10 primeiros termos
cont = 0        #Usado para limitar o loop ate 10
termo = int(input('Digite o termo(um numero): '))
razao = int(input('Digite a razao: '))
print(cores['verde'],termo , '-->', end= ' ')
while cont != 9: # enquanto for diferente de 9
    cont += 1
    termo+= razao
    print(f'{cores["verde"]}{termo} --> {cores["limpa"]}', end= '')
print(f'{cores["vermelho"]}FIM{cores["limpa"]}')


