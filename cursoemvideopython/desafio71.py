                # Simulando caixa eletrnico
                # leia o valor a ser sacado e informe quantas cedulas de cada valor sera entregue
                # caixa possui apenas cedulas de 50,20,10,1 R$
from cordes import cores,desafio
desafio(71)
while True:         # MINHA SOLUÇÃO
    print(f'{" CAIXA ELETRONICO ":-^40}')
    saque = int(input('Digite o Valor a ser sacado (0 para sair):'))
    total = saque
    ced50 = 50
    ced20 = 20
    ced10 = 10
    ced1 = 1
    total_ced50 = total_ced20 = total_ced10 = total_ced1 = 0
    if saque == 0:
        print(f'{"PROGRAMA ENCERRADO" :=^40}')
        break
    while True :
        if total >= ced50:
            total -= ced50
            total_ced50 +=1
        elif total >= ced20:
            total -= ced20
            total_ced20 +=1
        elif total >= ced10:
            total -= ced10
            total_ced10 +=1
        elif total >= ced1:
            total -= ced1
            total_ced1 +=1
        else:
            break
    print(f'Voce quer sacar {saque:.2f} R$ e Recebera >>>')
    print(f'{total_ced50} notas de {ced50} R$\n{total_ced20} notas de {ced20} R$')
    print(f'{total_ced10} notas de {ced10} R$\n{total_ced1} notas de {ced1} R$')

print('='*40)       #Solução guanabrara achei mais eficiente
print(f'{"CAIXA ELETRONICO":^40}')
print('='*40)
valor = int(input('Digite um valor para sacar: R$'))
total = valor       #Guarda o valor
ced = 50        #Valor da cedula
total_ced = 0       #Contador da cedula
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0 :
            print(f'{total_ced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('='*40)
print(f'OBRIGADO POR USAR O CAIXA , VOLTE SEMPRE, ATE LOGO!!!')
