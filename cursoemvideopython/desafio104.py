from cordes import desafio,quebra_de_linha,cores
desafio(104)
                # crie uma função chamada leiaint()
                # essa função vai funcionar como a função input so que so recebera numeros
                # imprima o valor se for numero se nao da erro
def leiaint(msg):
    while True:
        a = input(msg).strip()
        if len(a) == 0:
            print(f'{cores["vermelho"]}Erro! Digite um numero valido.{cores["limpa"]}')
        elif a in '0123456789':
            return a
        else:
            print(f'{cores["vermelho"]}Erro! Digite um numero valido.{cores["limpa"]}')

   

n = leiaint('digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
print(quebra_de_linha)

# jeito do guanabara  (achei o meu com a mesma eficiencia , tentei faze isso que ele fez e nao soube como kkkk ai codeide outro jeito)
def leiaint1(msg):
    ok = False
    Valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'{cores["vermelho"]}Erro! Digite um numero valido.{cores["limpa"]}')
        if ok:
            break
    return valor

n1 = leiaint1('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n1}')