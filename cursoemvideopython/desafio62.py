from cordes import cores , desafio , quebra_de_linha
desafio(62)     # Super Progressão Aritimetica 
termo = int(input('digite um numero: '))
razao = int(input('digite uma razao para o termo digitado: '))
acum = 10       # parametro para sequecia de laços
stop = ''
cont = 0        # acumulador
while stop != 'encerrar':
    for pa in range(acum):
        cont += 1
        print(f'{cores["verde"]}{termo} --> {cores["limpa"]}', end= '')
        termo += razao
    print(cores['vermelho'],'STOP', cores['limpa'])
    opção = int(input('digite quantos termos ainda quer ver: '))
    acum = opção
    if opção == 0:
        stop = 'encerrar'
        print(f'{cores["verde"]}Progressao finalizada com {cont} termos mostrados.{cores["limpa"]}')

                # Codigo do guanabara abaixo
print(quebra_de_linha)
termo = int(input('Digite um numero: '))
razao = int(input('Digite a razao para o termo digitado: '))
acum = 0
quant = 10
cont = 1
while quant != 0:
    acum = acum + quant
    while cont <= acum:
        print(f'{termo} --> ', end= '')
        termo += razao
        cont += 1
    print(f'STOP')
    quant = int(input('quantos termos voce ainda quer ver? >>> '))

print(f'progressao finalizada com {acum} mostrados')
