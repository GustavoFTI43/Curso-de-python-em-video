cores = {
    'subazul' : '\033[4;34m' ,
    'vermelho' : '\033[31m' ,
    'verde' : '\033[32m' ,
    'preta' : '\033[7;97m' ,
    'amarelo' : '\033[33m' ,
    'limpa' : '\033[m'
}


def desafio(a):
    if a <= 35:
        print(f'{cores["subazul"]}{"Ola , seja bem Vindo Ao mundo 1":=^74}{cores["limpa"]}')
        print(f'{cores["preta"]}','>'*30 , f'Desafio {a}' , '<'*30, f'{cores["limpa"]}')
    elif a > 35 and a < 71:
        print(f'{cores["subazul"]}{"Ola , seja bem Vindo Ao mundo 2":=^74}{cores["limpa"]}')
        print(f'{cores["preta"]}','>'*30 , f'Desafio {a}' , '<'*30, f'{cores["limpa"]}')
    elif a > 71:
        print(f'{cores["subazul"]}{"Ola , seja bem Vindo Ao mundo 3":=^74}{cores["limpa"]}')
        print(f'{cores["preta"]}','>'*30 , f'Desafio {a}' , '<'*30, f'{cores["limpa"]}')


quebra_de_linha = '-=' * 37