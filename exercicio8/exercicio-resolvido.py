salarioHora = float(input("Digite o valor do seu salário por hora (EX: 25.50): "))
horasTrabalhadasMes = int(input("Digite a quantidade de horas trabalhadas por mês (Número Inteiro): "))

salario = salarioHora * horasTrabalhadasMes

print(f"O seu salário do mês é R$ {salario:.2f}.")
