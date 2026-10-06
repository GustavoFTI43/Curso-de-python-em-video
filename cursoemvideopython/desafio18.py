from cordes import desafio
desafio(18)
                # leia um algulo e mostre o resultado de seno , cosseno e tanjente
import math 
numero = int(input('digite um angulo em graus:'))
rad = math.radians(numero)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'{rad: .4f} \n Seno {sen: .4f}. \n Cosseno {cos: .4f}. \n Tangente {tan: .4f}')