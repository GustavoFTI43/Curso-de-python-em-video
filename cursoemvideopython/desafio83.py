from cordes import desafio,cores , quebra_de_linha
desafio(83)
                # leia expressoes aritimeticar com parenteses
                # analise se os parentes aberto,fechado esta na ondem correta
expressao =  input('digite uma expressão: ').strip()
a = expressao.count('(')
b = expressao.count(')')
c = a + b 
if c == 0:
    print('Expressão correta')
elif '(' not in expressao or ')' not in expressao or c % 2 == 1:
    print('Expressão incorreta')
elif '(' and ')' in expressao and c % 2 == 0:
    print('Expressão correta')

                # Jeito do guanabara
print(quebra_de_linha)
print(f'{"jeito do guanabara":-^74}')
expr = str(input('Digite a expressão:')).strip()
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()     # Remove o ultimo item da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta')
else:
    print('expressão incorreta')