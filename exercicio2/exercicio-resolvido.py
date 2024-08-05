"""
Exercicio 2. Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.
"""

ano_de_nascimento = int(input('Digita o ano do seu nascimento'))
ano_atual = 2024
idade_atual = ano_atual - ano_de_nascimento
print(f'Você tem {idade_atual} anos')
