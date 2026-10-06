from cordes import desafio
desafio(113)
                # crie 2 funçoes dentro de um novo modulo exe113 no pacote pkdesafios
                # 1 função deve ler numeros inteiros com tratamento de erros/exceçoes
                #2 função deve ler numeros reais com tratamento de erros/exceçoes

from pkdesafios.exe113 import leiaint , leiafloat
a = leiaint('Numero inteiro: ')
b = leiafloat('Numero real: ')
print(f'O numero inteiro foi {a} e o real foi {b}')