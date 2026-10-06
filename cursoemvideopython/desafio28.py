from cordes import desafio
desafio(28)
                # sortear numero de 0 a 5 e tentar adivinhar qual numero foi sorteado
from random import choice       # modulo de sorteio random
numeros = [0,1,2,3,4,5]     # lista com numeros 
numero_sorteado = choice(numeros)       # sorteio 
numero_usuario = int(input('adivinhe o numero sorteado >> '))       # entrada do numero a ser adivinhado
if numero_sorteado == numero_usuario:       # condição se acertou o numero ou não
    print(f'parabens voce adivinhou!!!\nO numero {numero_sorteado} que foi sorteado')
else:
    print('não foi dessa vez')