from cordes import desafio
desafio(35)  
                # leia 3 linhas retas com comprimentos diferentes e verifique se é possivel formar um triangulo
while True:     #loop de while para executar codico variass vezes 
    print('-' * 30 )        # separar codigo
    l1 = float(input('digite o comprimento da linha 1 em metros: '))        #recebendo valores
    l2 = float(input('digite o comprimento da linha 2 em metros: '))
    l3 = float(input('digite o comprimento da linha 3 em metros: '))
    if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):        # condição verdadeira
        print('sim é possivel formar um triangulo')
    else:       # se falsa 
        print('não é possivel formar triangulo')

    R = input('\nQuer testar novamente ? (S/N):').strip().upper() 
    if R == 'N' or R == 'NAO' or R == 'NÃO':        # encerra programa se verdadeiro
        print('TESTE ENCERRADO, ATÉ LOGO !')
        break       # iterrompe loop 
'''
print('TESTE DE TRY/EXCEPT') #try (tente) except (caso de erro ...)
try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou o número {numero}")    
except ValueError:
    print("Isso não é um número válido! Tente novamente.")
    
print("O programa continua rodando aqui embaixo normalmente...")
# ele serve para deixar o seu sistema robusto, tratando as falhas com mensagens amigáveis em vez de exibir aquele texto vermelho de erro técnico para o usuário.


cores = {
    'subazul' : '\033[4;34m' ,
    'vermelho' : '\033[31' , 
    'preta' : '\033[7;30' , 
    'limpa' : '\033[m'
}
print(f'{cores["subazul"]} Ola Mundo!!!{cores["limpa"]}')
'''