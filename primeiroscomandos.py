'''print('ola gustavo , welcome to new curso ')

customensal = 2200
investmento = 100
ganhos = 2500
if ganhos > 2200:
    print("invista 100 reais") # Bloco de código a executar se a condição for verdadeira instruções
    
else:
        print("fazer renda extra")

saldo = customensal - ganhos 
print(saldo, "saldo")
listadecoisasafazer= ["estudar programação","estudar ingles"]
for tarefa in listadecoisasafazer:
    print(tarefa)
    
multiplicaçao = [500,100,300]
for item in multiplicaçao:
    print(item * 3)

for i in range(2):
    print("fundamentos abaixo ")
    
    
a = 10
b = 3

#aritmética
soma = a + b   # 13
subtracao = a - b    # 7
multiplicacao = a * b    # 30
divisao = a / b   # 3.333333333
divisao_inteira = a // b   # 3
modulo = a % b   # 1
exponenciacao = a ** b   # 1000
resultado_de_equação = [soma,subtracao,multiplicacao,divisao,divisao_inteira,modulo,exponenciacao]
for R in resultado_de_equação:
    print(R) #loop for 


# Comparação
igual = a == b  #False
diferente = a != b   #True
maior_que = a > b   #True
menor_que = a < b   #False
maior_ou_igual = a >= b #True
menor_ou_igual = a <= b #False
print(igual,diferente,maior_que,menor_que,maior_ou_igual,menor_ou_igual)

#Lógicos
resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False
resultado_not1 = not (a < 5)   # True
print(resultado_and,resultado_or,resultado_not,resultado_not1)

#Condicionais
nota = 100
if nota == 100:
    print("aluno nota 100")
elif nota >=90 and nota <=99:
    print("excelente")
elif nota >=80: 
    print("muito bom")
elif nota >=70:
    print("bom")
else:
    print ('tenta denovo')
 
#loops 
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:  
    print(fruta)
    
for numero in range(1, 5): #range ( start, stop)
    print(numero* 2)

for numero in range(0, 20, 2): #range (start, stop, step)
    print (numero)
    

contador = 0 
while contador <=5: # quanto o contador de 1 em 1 chegar a 5 ele interrope o loop pois passa a aser falso 
    print(contador)
    contador += 1  # instrução de contagem 
    
#controle de loops 
#break é acionado se a função if chegar a valor condicionado 
contador = 0
while True:
    print(contador)
    contador += 1
    
    if contador == 3:
        break
    
#continue
for i in range(10):

    if i % 2 == 0:
        continue
    print(i) 

# listas 
nome = ['gustavo','emilly','adriel'] # leia a função que quer executar a partir desta lista podendo sortear e adicionarmais nomes 
função = input('para adicionar digite ad e para sortear digite s')
ad = nome.append(input('digite o nome que quer adicionar'))
s = int(input('digite o numero'))
if função == ad:  
    print(ad)
else :
    print('erro')
    
if função == s:
    print(s)
    
elif s == 1:
    print(nome[0]) 
elif s == 2:
    print(nome[1])
elif s == 3:
    print(nome[3])
else :
    print ('erro')

print(nome)

primeiros comandos
'''