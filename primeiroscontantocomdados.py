'''def calcular_desconto(preco, desconto):
    resultado =preco - (preco * (desconto / 100))
    return resultado

desconto = int(input('digite desconto'))
preco = int(input('digite preço'))

final = calcular_desconto(preco, desconto)
print(f'voce pagara {final} reais neste produto')

                    # criando lista 
nomes = ['gustavo','nathaly','adriel']
                    # definindo função de saudação
def saudacao(nome):
    print(f'ola {nome}, seja bem vindo')
                    # procurando objeto na lista 
for nome in nomes:
    saudacao(nomes) 

def maior_numero(numero):
    maior = numero[0]
    for num in numero:
        if num > maior:
            maior = num 
    return maior
        
numeros = [1,2,3,4,5,6]
resultado = maior_numero(numeros)
print(resultado) 
                #dicionario
pessoa = {
    'nome' : 'gustavo',
    'idade' : 25,
}

pessoa['cidade'] = 'sao paulo'

print(pessoa['cidade'])
for chave, valor in pessoa.items():
    print(f'{chave},{valor}') '
                    # lista dicionario 
cadastro = [
    {'nome': 'gustavo', 'idade': 25},
    {'nome': 'nathaly', 'idade': 20},
    {'nome': 'adriel',  'idade': 13}
]
                    #definindo função
def listar_pessoas(lista):
    for pessoa in lista:
        print(f'Nome : {pessoa["nome"]} | Idade : {pessoa["idade"]}')

listar_pessoas(cadastro) 

print('ola', end= '')
print('mundo')

# lista com 4 produtos
lista = ['banana','pera','maça','uva']
print(f'Primeira : {lista[0]}') 
print(f'ultima : {lista[-1]}')
lista.append('morango') #adcionado novo objeto
print(f'nova lista tem {len(lista)} items') 

# criando dicionario
produto = {
    'nome' : 'motorola',
    'preco' : 1000 , 
    'estoque' : 10
}

produto['categora'] = 'smartphones' # adicionando nova categoria
produto['preco'] = 2000 # atualizando preço de dicionario 
print('=' * 50)
for chave, valor in produto.items():
    print(f'{chave} = {valor}')

# lista de dicionarios

estoque = [
    {'nome': 'notebook' , 'preço' : 1500 , 'estoque' : 7} ,
    {'nome': 'caixa de som' , 'preço' : 300 , 'estoque' : 7 } ,
    {'nome': 'mause' , 'preço' : 70 , 'estoque' : 7 }
]
# função que resumi valor total de produto em estoque 

def resumo_estoque(estoque):
    for produto in estoque:             # percorrendo cada dicionario dentro da lista 
        total = produto['preço'] * produto['estoque']
        produto['total'] = total        #    adicionando novo item no dicionario 
        print(f'produto: {produto["nome"]} | Valor: {produto["preço"]} | Estoque: {produto["estoque"]} | Total: {produto["total"]}')

resumo_estoque(estoque)                 # chamada de função 


                    # Lista principal que armazena o cadastro
cadastro = []

while True:         # loop 
    nome = input('digite seu nome ou "sair" para encerrar :').lower().strip()
    if nome == 'sair':
        print('\033[4;31m cadastro encerrado')
        break       #break se condição verdadeira

    idade = int(input('sua idade'))
    email = input('digite seu email')

                    # dicionaro de cadastro induvidual
    cad_individual = {
        'nome' : nome ,
        'idade' : idade ,
        'email' : email
    }
    cadastro.append(cad_individual)
    print('>>>>> cadastro salvo <<<<<')

print('\n>>>>> Lista de cadastros <<<<<')
for pessoa in cadastro:
    print(f'NOME : {pessoa["nome"]} | IDADE : {pessoa["idade"]} | EMAIL : {pessoa["email"]}')

'''