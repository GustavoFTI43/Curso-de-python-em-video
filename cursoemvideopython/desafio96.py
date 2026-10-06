from cordes import desafio,quebra_de_linha
desafio(96)
                # crie e defina uma função para calcular area de um terreno retangular
                # receba os valores
                # mostre a area do terreno 
def area(l , c):
    r = l * c
    print(f'A area do terreno de {l}X{c} é de {r} metros quadrados.')

print('Calculando metragem de terreno')
print(quebra_de_linha)
while True:
    comprimento = float(input('Qual o comprimento do terreno: ').strip())
    largura = float(input('Qual a largura do terreno: ').strip())
    area(largura,comprimento)
    opçaõ = input('Quer continuar ? [S/n]').strip().upper()[0]
    if opçaõ in 'Nn':
        print('>>>>> fim <<<<<')
        break

    