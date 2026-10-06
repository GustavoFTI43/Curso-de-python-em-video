from cordes import desafio
               #estrutura de repetição for     
desafio(46)     #contagem regresiva de 10 a 0 com intervalo de 1 seg
from time import sleep

for i in range(10 , -1 , -1):
    print(i)
    sleep(1)
print('************************ \n*******CA-BOOOOM********\n************************')
sleep(2)
desafio(47)     #mostre todos numeros pares de 1 a 50
for i in range(0 , 51, +2):
    print(i)