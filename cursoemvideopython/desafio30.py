from cordes import desafio
desafio(30)
                # ler um numero inteiro e mostrar se é impar ou par
numero = int(input('digite um numero inteiro'))     # lendo numero
num = numero % 2        # calculo de impar ou par 
if num == 0 :       # condição com resultado par
    print('PAR')
else:       #se não impar
    print('IMPAR')