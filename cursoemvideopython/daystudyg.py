'''
print('seja bem vindo ao curso em video python')
                #digite seus codigos abaixo 
                #input(usado para ler oque foi digitado pelo usuario )
nome = input('digite seu nome')
print ('ola ', nome, ' prazer em conhecer voce!')

a = int(input('primeiro numero '))

b = int(input('segundo numero '))

print (a + b)
                #is opera identidade do valor atribuido , resultado verdadeiro ou falso 
a = input('digite algo ')
print(f'o tipo primitivo de {a} é ', type(a))
print('somente espaço', a.isspace( ))
print ('é alfabetico ',a.isalpha())
print('é numero', a.isnumeric())
print('é alphanumerico', a.isalnum())
print ('esta em maiuscula', a.isupper())
print('esta em minuscula', a.islower())
print ('esta capitalizada', a.istitle())
print ('junção de linha ', end= ' ')
print('para ver se da certo') 

n1 = int(input('digite o numero'))
print(type(n1))

n1= int(input('digite o numero'))

n2 = int(input('outro numero'))

s = n1 + n2
print('soma entre', n1,'e',n2, 'é igual a ', s)
print (f'a soma entre {n1} e {n2} é {s}') # .format ou f strig que é format covertido

a1 = input('digite algo ')
print(a1.isnumeric()) #operador de identidade (is...)

c1 = 5 + 3 * 2 
print(c1)
c2 = 3 * 5 + 4 ** 2 
print (c2)
c3 = 3 * (5+4) ** 2
print (c3)

nome = input('qual seu nome?')
print(f'prazer te conhecer{nome:=^20} !') #prazer te conhecer====== gustavo====== !

                # operadores aritimeticos

n1 = int(input('digite um numero '))
n2 = int(input('digite outro numero'))
s = n1 + n2
sb = n1 - n2
d = n1 / n2
p = n1 ** n2        #para raiz quadrada so elevar a 1/2 ou use a função pow de power 
m = n1 * n2
dint = n1 // n2 
rd = n1 % n2
print(f' soma {s}, \n subtração {sb}, \n divisão {d:.3f} ') 
print(f' potencia {p},\n divisão inteira {dint},\n multiplicação {m},\n resto divisao {rd} ')

                # day 2 studyng
                # Modulos
                # importação de modulos usa se From import ou import

import math 
num = int(input('digite o numero'))
raiz = math.sqrt (num)
print (f'a raiz de {num} é igual a {math.ceil(raiz)} ')

from math import sqrt , floor
nu = int(input('digite o numero '))
raiz1 = sqrt (nu)
print(f'a raiz de {nu} é {floor(raiz1)} ')

import random
nume = random.randint(1, 20)
print (nume)

                #day 3 studyng 
frase = ('   Eu sou a Verdade e a Vida   ')
print (frase[7:14])     #fatiando uma string 
print(len(frase))       #função mostra quantidade de caracteres 
print(frase.count('a'))     #indica quantas vezes encontrou a letra 'a'
print(frase.count('a',7,14))        #junçaõ de analise com fatiamento 
print(frase.find('dade'))       #indica o caracter que comecou a palavra 'dade'
print(frase.find('gu'))     #se indicar -1 é because nâo existe a string dentro da frase
print ('eu' in frase)       #retorna true ou false se existir a string na frase  OPERADOR (in)
print(frase.replace('Eu sou','Jesus é'))        #trocar/reposicionar as strings
print(frase.upper())        #transforma tudo em maiusculo 
print(frase.lower())        #transforma tudo em minusculo 
print(frase.capitalize())       #transforma tudo em minusculo e deixa a primeira letra maiuscula
print(frase.title())        #tranforma todas primeira letras das palavras em maiuculas , separando palavras pelos espaços
print(frase.strip())        #remove todos espaços das string do começo e do final da frase
A = frase.split()       #divide a string/frase em palavras separadas de uma nova lista e caracteres
print(A)        #mostra dividida
print(A[3])     #mostra a 3° string da lista que foi dividida
print('-'.join(A))
                # day 5 studyng
                # Condiçoes simples e compostas
carro = int(input('quantos anos vc tem seu carro? '))
if carro >= 15:
    print('seu carro ja esta velhinho em !!!')
else:
    print('seu carro ainda esta novo em !!!')
                # msm codigo simplificado 
tempo = int(input('tempo de uso de carro '))
print('carro novo'if tempo <=3 else 'carro velho')      # imprima para carro se o tempo for menor ou igual a 3 senao imprima carro velho (leitura do codigo)
print('>>> Fim <<<')
                #day 6 studyng
                # modelos de format - f string
a = 'gustavo'
i = 25
print('o {} tem {} de idade'.format(a,i))       #Versoes python 3
print(f'o {a} tem {i} de idade')        #Versoes python 3.6+
print('o %a tem %i de idade' % (a , i))     #Versoes python 2 

                #Day 7 studyng
                #Variaveis Compostas (tuplas) são imutaveis
lanche = ('hambugues','suco','pizza','pudim')
print(lanche)
print(lanche[0])
print(lanche[3])
print(len(lanche))
print('-' * 40)
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')
print('-' * 40)
for cont in range(0 , len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
a = (1 , 3 , 7)
b = (5 , 5 , 8 , 9)
c = a + b     # ou b + a
print(c)
print(c.index(3)) #Mostra em qual indice esta o numero 3
del(a,b)
print(a,b)

lista = ['casa',10,'cozinha','quarto']
lista.append('sala')
lista.insert(3,'banheiro')
lista.remove(10)
del lista[2]        #comando del deleta 
lista.pop(0)
lista.remove('quarto')      #procura da esquerda para direita e remove ao achar


numero = [18,3,6,4,9,8,42,7,5]
numero.sort(reverse=True)       #organiza de froma reversa
for c , v in enumerate(numero):     # com enumerate voce consegue exibir o valor de sequencia de acordo com itens da lista
    print(f'na posição {c} encontrei o valor {v}!')
print('acabou')
a = [1,4,7,9]
c = a       # se torna 2 listas identicas porem sao iterligadas e nao copiadas , se alterar ela altera as 2 listas
b = a[:]        # diferente de apenas receber a , ele recebe os valores de a sendo uma copia da lista a
b[2] = 8
print(f'lista a {a}\nlista b {b}')
                #Outro exemplo de duplicação e copia 
teste = list()
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)       # O fatiamento dentro do append [:] esta age como uma copia e corta a relação da edição podendo editar uma sem mecher na outra
teste1 = list()
teste1.append('gustavo')
teste1.append(40)
galera1 = list()
galera1.append(teste)
teste1[0] = 'maria'
teste1[1] = 22
galera1.append(teste)
print(galera1)      # ele imprimi 2 vezes o mesmo valor por nao ser uma copia 

                # day 8 studyng
# dicionario
pessoas= {'nome':'gustavo','idade': 22}
print(f' o {pessoas["nome"]} tem {pessoas["idade"]}')
pessoas['sexo'] = 'masculino'
del pessoas['idade']
pessoas['peso'] = 58.8
for k , v in pessoas.items():
    print(f'{k} = {v}')
# lista de dicionarios
pessoa1 = {'nome':'gustavo','idade':22}
pessoa2 = {'nome':'emy','idade': 20}
pessoa= []
estados = dict()
brasil = list()
for i in range(2):
    estados['nome'] = input('digite o estado')
    brasil.append(estados)       # metodo copy utilizado para nao interliga as entrada de valor do dicionario como na lista seria [:] assim podendo criar 2 diconarios diferentes mas q sao copyas simples
estado = brasil.copy()
print(id(estado) , id(brasil))   # o id das listas é diferente porem do item dentro das lista é o mesmo pois sao uma copia rasa
# para vc mecher nos item de estado sem alterar de brasil tem q fazer uma copia profunda usando deepcopy() 

                # day 9 studyng
#interactive help
help()      # mostra uma bibliotaca ou função , mostra oq elas faz
print('função'.__doc__) # mostra o doc desta função
# docsstring 
def contador(i , f , p):
    
    Faz uma contagem e mostra na tela >>
    para i : inicio da contagem
    para f : fim da contagem
    para p : passo da contagem
    return : sem retorno

    c = i
    while c <= f:
        print(f'{c}' , end=' ')
        c +=p
    print('Fim')
i = 2
f = 10
p = 2
help(contador)      # vc coloca um comentario usando 3 aspas e isso auxiliara quem não sabe como funciona
                    # a utilizar a função explicando oq parametros a seres recebidos
# escopo de variaveis
# bomo podemos ver no codigo acima , c recebe i de inicio
# porem c nao existe fora da função entao ( c passa a ser variavel local que so existe naquele bloco , se eu chamr ela fora daquele bloco da erro)
# porem i que esta fora da função , dentro da função ainda é i entao ( i é uma variavel global pois roda por qualqer parte do codigo)
# caso aja duvida de um print nas variaveis dentro e fora da função e vera que c nao existe fora da função
def soma(b):
    global a    # faz com que o valor de a dentro da função seja global ou seja a variavel fora da função ja nao é mais valida
    a = 2       # sem global , a é 2 dentro e fora é 3
    b += 4      # não existe fora
    c = 2
    print(f'A é {a } dentro')
    print(f'B é {b } dentro')
    print(f'c é {c } dentro')


a = 3
soma(a)
print(f'A é {a } fora')
print('b e c nao existe fora')

# retornode resultados
def soma (a = 0 , b = 0 , c = 0):
    s = a + b + c
    return s
r1 = soma(7,8,9)
print(f'{r1}')
'''
 # day studyng 5 
 # modularização
 # criando um pacote
''' meu_pacote/             <-- (New Folder)
    ├── __init__.py         <-- (New File)
    ├── modulo1.py          <-- (Adicionar módulos)
    └── modulo2.py
    '''

# day sturdyng 6
# tratamento de erro e 
try:            # Tente fazer a operação abaixo
                # exept para se o programa der problema podendo usar o else para acerto que é opcional
                # finally é oq acontece sempre idependente do erro ou do acerto

    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou!')
except ZeroDivisionError:
    print('Não é possivel dividir um numero pro zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
except Exception as erro:       # este é um except generico ou seja para mostrar erro e class
    # dentro do excep chamamos o exception que criou uma variavel para erro neste caso de class 
    print(f'problema encontrado foi {erro.__class__}')
else:
    print(f'o resultado é {r}')
finally:
    print('Obrigado volte sempre')

