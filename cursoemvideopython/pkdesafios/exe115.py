def tituloformatado(txt , vezescr = 1):
    '''
    => recebe uma mensagem e quantidade de vezes que repetira o len(txt)
    cr para : somar o caracter total do txt formatado
    imprimi txt formatado com linhas para titulos
    '''
    cr = (len(txt) + 4) * vezescr
    print(f'{"=" * cr}\n{txt:^{cr}}\n{"=" * cr}')

def linha():
    print('-' * 54)

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

def menu(lista):
    
        tituloformatado('MENU PRINCIPAL' , 3)
        for c , v in enumerate(lista):
            print(f'\033[33m{c+1} - \033[34m{v}\033[m')
        linha()
        opção = leiaint('Sua opçao: ')
        return opção

def arqExiste(nome):
    try:
        a = open(nome , 'rt') # verifica sse arquivo existe e retorna true se existir
        a.close()
    except FileNotFoundError:  
        return False
    else:
        return True

def criarArq(name):
    try:
        a = open (name , 'wt+') # cria arquivo novo
        a.close()
    except:
        print('Houve um Erro na criação do arquivo')
    else:
        print(f'{name} criado com sucesso')

def lerArquivo(name):       # ler as informacoes dentro do arquivo
    try:
        a = open(name , 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        tituloformatado('PESSOAS CADASTRADAS' , 2)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n' , '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo , nome , idade):
    try:
        a = open(arquivo , 'at')
    except:
        print('Houve um Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um Erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adiconado')
            a.close()

