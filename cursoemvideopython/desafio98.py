from cordes import desafio , quebra_de_linha
desafio(98)
                # Crie uma função chamada contador que receba 3 parametros: inicio , fim , passo
                # realize 3 contagens atraves dessa função 
                # 1º de 1 a 10 de 1 em 1
                # 2º de 10 a 0 de 2 em 2
                # 3º contagem do jeito que preferir
from time  import sleep
def contador(i , f , p):
    print(quebra_de_linha)
    if p == 0:
        p = 1
    if p < 0:
        p = - p
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f :
        for cont in range(i , f-1 , -p):
            print(f'{cont} ', end='' , flush=True)
            sleep(0.5)
    
        print('Fim!!!')
    else:
        for cont in range(i , f+1 , p):
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
        
        print('Fim!!!')
''' 
contador(1 , 10 , 1)
contador(10 , 0 , 2)
print(quebra_de_linha)
inicio = int(input(f'Agora é sua vez de personalizar a contagem!\nInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
print(quebra_de_linha)
'''
print('Jeito guanabara')        # com while 

def contador1(i , f , p):
    if p == 0 :
        p = 1
    if p < 0 :
        p = - p
    print(quebra_de_linha)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:
        cont = i 
        while cont > f-1:
            print(f'{cont} ', end='', flush=True)
            cont -=p
            sleep(0.5)
        print("fim!!!")
    else:
        cont = i
        while cont < f+1:
            print(f'{cont} ', end='', flush=True)
            cont +=p
            sleep(0.5)
        print("fim!!!")

contador1(1 , 10 , 1)    
contador1(10, 0 , 2)
print(quebra_de_linha)
inicio = int(input(f'Agora é sua vez de personalizar a contagem!\nInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador1(inicio,fim,passo)