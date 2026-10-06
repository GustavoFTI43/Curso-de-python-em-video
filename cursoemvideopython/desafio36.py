from cordes import cores,desafio,quebra_de_linha
desafio(36)
                # receba os valores da variaveis salario, valor casa e anos a pagar
valor_casa = float(input('qual valor da casa: '))
salario = float(input('seu salario é: '))
anos = int(input('quantos anos ira pagar: '))
                #funçao para calcular emprestimo e aprovação
print(quebra_de_linha)
def emprestimo(casa , salario , anos):
    prestacao = casa / (anos * 12)
    criterio = salario * 0.30
    if prestacao >= criterio:
        print(f'{cores["vermelho"]}>>>>> Emprestimo Negado <<<<<{cores["limpa"]}')
    elif prestacao < criterio:
        print(f'{cores["subazul"]}Parabéns!!!\nSeu emprestimo foi aprovado{cores["limpa"]}')
    else:
        print('')
    return prestacao
valor_prestação = emprestimo(valor_casa , salario , anos)
print(f'Para Comprar uma casa de {valor_casa}, Você precisara pagar o valor da pretação de {valor_prestação:.2f}')
