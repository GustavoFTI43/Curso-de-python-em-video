from cordes import desafio
desafio(13)
                # leia o salario atual do seu funcionario e aplique de aumento de 15% 
salario = float(input(' digite seu salario atual '))
pc_aumento = salario * 0.15
total = salario + pc_aumento 
print (f'Parabens seu salario agora é R${total}')