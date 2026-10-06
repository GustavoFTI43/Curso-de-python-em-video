from cordes import  desafio
desafio(17)
                # calcule o cateto aposto e adjacente
from math  import pow, sqrt
Cop = float(input('digite o cateto oposto: '))
cop1 = pow (Cop,2)
Cad = float(input('digite o cateto adjacente: '))
cad1 = pow (Cad,2)
print(f'Cateto aposto {cop1} \nCateto adjacente {cad1}')
                # calcule a hipotenusa 
H = sqrt(cop1 + cad1)
print(f'o valor da hipotenusa é {H}')
                # tambem tem a opção de modulo direto 
from math import hypot
ca = float(input(' cateto ad: '))
co = float(input('cateto op:'))
h = hypot (co , ca )
print(h)
