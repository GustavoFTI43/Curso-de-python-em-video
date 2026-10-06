from cordes import cores,desafio
                # Sequencia De Fibonacci
desafio(63)
termo = int(input('Digite quantos termos voce quer ver >>> '))
a = 0
b = 1
cont = 0
while cont != termo:
    print(f'{cores["verde"]}{a} --> {cores["limpa"]}', end= '')
    a , b = b, a + b        # Atribuição multipla de variaveis
    cont += 1
print(f'{cores["vermelho"]}FIM{cores["limpa"]}')

                # Tambem é possivel fazer com for
termo1 = int(input('Digite quantos termos voce quer ver >>> '))
a1 = 0
b1 = 1
for t in range(termo1):
    print(f'{cores["verde"]}{a1} --> {cores["limpa"]}', end= '')
    a1 , b1 = b1 , a1 + b1
print(f'{cores["vermelho"]}FIM{cores["limpa"]}')