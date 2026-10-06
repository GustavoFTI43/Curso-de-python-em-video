from cordes import desafio
desafio(34)
                # ler salario e calcular valor de aumento , > que 1250R$ 10% de aumento se < aumento de 15%
salario = float(input('digite o salario: '))        # lendo salario
base = float(1250.00)       # media base para ajuste 
if salario >= base:     # condições para ajuste salario e impreção de salario ajustado 
    Rsa = (salario / 100) * 10      # calculo para 10%
    salario = Rsa + salario
    print(f'você teve um reajuste de salario para {salario}R$')
elif salario < base:
    Rsb = (salario / 100) * 15      # calculo para 15%
    salario = Rsb + salario
    print(f'você teve um reajuste de salario para {salario}R$')
else:
    False 