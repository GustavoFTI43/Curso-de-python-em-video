from cordes import desafio
desafio(55)
                #leia o peso de 5 pessoas e veja qual é o maior peso e o menor peso
dados = [ ]
for p in range(1,6):
    peso = float(input(f'digite o peso da {p}° pessoa: '))
    dados.append(peso)
dados_ordenados = sorted(dados)     #sorted orgaiza a lista do menor para maior
maior = dados_ordenados[-1]
menor = dados_ordenados[0]
print(f'dentre essas pessoas o maior peso é {maior} e o menor é {menor}')