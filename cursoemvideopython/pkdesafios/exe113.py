def leiaint(msg):
    '''
    => recebe mensagem para int(input())
    retorn n_int : valor inteiro ou imprimi erros/exceçoes
    '''
    while True:
        try:
            n_int = int(input(msg))
        except ValueError:
            print(f'\033[31mErro : Digite um valor inteiro \033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mErro : nenhum valor digitado \033[m')
            return 0
        else: 
            return n_int

def leiafloat(msg):
    '''
    => recebe mensagem para float(input())
    retorn n_float : valor real ou imprimi erros/exceçoes
    '''
    while True:
        try:
            n_float = float(input(msg))
        except ValueError:
            print(f'\033[31mErro : Digite um valor real \033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mErro : nenhum valor digitado \033[m')
            return 0
        else:
            return n_float
