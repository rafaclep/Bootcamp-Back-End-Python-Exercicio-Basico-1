#Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício

print("**** Quantas calorias foram queimadas no exercício? ****")
horaExercicio = int(input("Quantas horas de exercício foram feitas essa semana? "))
gastoExercicio = horaExercicio*(5*60)
exercicioMes = gastoExercicio*4

print(f"O gasto de caloria em uma semana foi em média de {gastoExercicio} calorias e no mês foi de {exercicioMes}")
