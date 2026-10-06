from cordes import cores,desafio,quebra_de_linha
desafio(44)
                # calcular valor de produto,considerar preço e condiçao de pagamento
produto = input('nome produto: ')
valor = float(input('Qual valor do produto: R$').strip())
M_pagamento = int(input('(1) A VISTA/CHEQUE\n(2) DEBITO\n(3) CRÉDITO ÁVISTA/PARCELADO\nQual opçao deseja: '))
print(quebra_de_linha)
if M_pagamento == 1:
    saldo = valor - (valor * 0.10)
    print(f'VOCÊ PAGARA {saldo}R$ DE {valor}R$ POIS TEVE DESCONTO DE 10%')
elif M_pagamento == 2:
    saldo = valor - (valor * 0.05)
    print(f'VOCÊ PAGARA {saldo}R$ DE {valor}R$ POIS TEVE DESCONTO DE 5%')
elif M_pagamento == 3:
    parcelas = int(input('QUANTAS VEZES DESEJA PARCELAR: ').strip())
    if parcelas <= 2:
        print(f'OK , GERANDO PAGAMENTO DE {valor}R$','.' * 30)
    elif parcelas >= 3 :
        saldo = valor + (valor * 0.20)
        parcelado = saldo / parcelas
        print(f'SEU PRODUTO SAIRA POR {parcelas}x DE {parcelado}R$\nSOMANDO UM TOTAL DE {saldo}R$ POIS TEVE JUROS DE 20%')
else:
    print(f'{cores["vermelho"]}ERRO!!!\nSELECIONE UMA DAS OPÇOES PARA PAGAR{cores["limpa"]}')
