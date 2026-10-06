from cordes import cores,desafio
desafio(59)
                # leia 2 numeros e realize a operação selecionada das opçoes sugeridas
stop = ''
while stop != 'encerrar':
    num1 = float(input('digite o 1° numero: '))
    num2 = float(input('digite o 2° numero: '))
    stop = ''
    while stop != 6 and stop != 'encerrar':
        opção = int(input('[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir\n[5] Maior\n[6] Novos Numeros\n[0] Encerrar\nESCOLHA A OPERAÇÃO QUE DESEJA REALIZAR: '))
        if opção == 1 :
            resultado = num1 + num2
            print(f'{cores["verde"]}voce escolheu Somar\nO resultado é {resultado}{cores["limpa"]}')
        elif opção == 2:
            resultado = num1 - num2
            print(f'{cores["verde"]}voce escolheu Subtrair \nO resultado é {resultado}{cores["limpa"]}')
        elif opção == 3:
            resultado = num1 * num2
            print(f'{cores["verde"]}voce escolheu Multiplicar\nO resultado é {resultado}{cores["limpa"]}')
        elif opção == 4:
            resultado = num1 / num2
            print(f'{cores["verde"]}voce escolheu Dividir\nO resultado é {resultado}{cores["limpa"]}')
        elif opção == 5:
            if num1 > num2:
                print(f'{cores["verde"]}O numero maior é o {num1}{cores["limpa"]}')
            else:
                print(f'{cores["verde"]}O numero maior é o {num2}{cores["limpa"]}')
        elif opção == 6:
                    print(f'{cores["amarelo"]}Digite novos numeros{cores["limpa"]}')
                    stop = opção
        elif opção == 0:
             stop = 'encerrar'

        else:
             print(f'{cores["vermelho"]}Opção digitada invalida. Tente novamente!!!{cores["limpa"]}')
        

print('Programa Encerrado!!!')