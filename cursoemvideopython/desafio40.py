from cordes import cores,desafio,quebra_de_linha
desafio(40)
                #calcular media e condição de aprovação
print(f'{cores["preta"]}', '.' * 30 , 'verifique aprovação' , '.' * 30 , f'{cores["limpa"]}')
nota_1 = float(input('Nota primeiro semestre: '))
nota_2 = float(input('Nota segundo semestre: '))
media = (nota_1 + nota_2) / 2
print(quebra_de_linha)
if media >= 7:
    print(f'{cores["verde"]}Parabens você foi aprovado!!!{cores["limpa"]}\nSua media foi {media}')

elif media < 5:
    print(f'{cores["vermelho"]}REPROVADO !!!{cores["limpa"]}\n Sua media foi {media}')

elif media >= 5 and media <7:
    print(f'{cores["amarelo"]}Você esta de RECUPERAÇÃO\nSua media foi {media}{cores["limpa"]}')