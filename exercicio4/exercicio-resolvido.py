# Exercicio 4. Receba do usuário a quantidade de litros de combustível consumidos e
# a distância percorrida. Calcule e imprima o consumo médio em km/l.


litros_consumidos = float(
    input('Informe a quantidade de litros de combustível consumidos:'))
distancia_percorrida = float(
    input('Informe a distância percorrida em quilômetros:'))
consumo_medio = distancia_percorrida / litros_consumidos
print(f'O consumo médio é de {consumo_medio:.2f} km/l')
