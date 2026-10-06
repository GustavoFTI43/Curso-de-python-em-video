                # leia nome, idade e sexo de varias pessoas
                # mostre os maiores de 18 , quantos são homens e quantas mulheres tem menos de 20 anos
from cordes import cores, desafio
desafio(69)
homen = mulheres_menor20 = maiores_18 = 0
while True:
    print('-' * 40,'\n   CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = ''
    while not idade.isnumeric():
        idade = (input('Digite a Idade: '))
    idade = int(idade)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo: [M/F] '))[0].upper().strip()
    print('-=' * 40)
    if idade > 18:
        maiores_18 +=1
    if sexo in 'Mm':
        homen +=1
    if sexo in 'Ff' and idade < 20:
        mulheres_menor20 +=1
    opçao = ' '
    while opçao not in 'SN':
        opçao = input(f'{cores["verde"]}Quer continuar{cores["limpa"]}[S/N]: ')[0].upper().strip()
    if opçao == 'N':
        print('-=' * 40)
        print(f'{cores["vermelho"]}PROGRAMA ENCERRADO{cores["limpa"]}')
        break
print(f'{cores["amarelo"]}Foram cadastrado {homen} homens\n{maiores_18} pessoas são maiores de 18\nApenas {mulheres_menor20} mulher(es) sao menores de 20 anos{cores["limpa"]}')


