'''
exercício 1 do Desafio 1 - Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão.
'''

import os
import platform
from typing import Final
from typing import Any

COR_BRANCA: Final[str] = '\033[0;0m'
COR_BRIGHT_AMARELA: Final[str] = '\033[93m'
COR_VERDE: Final[str] = '\033[32m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'


# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

def bright_amarelo(conteudo: Any) -> Any:
    '''
    Colore o texto informado em amarelo brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_AMARELA}{conteudo}{COR_BRANCA}"

def verde(conteudo: Any) -> Any:
    '''
    Colore o texto informado em verde.
    Retorna o texto colorido.
    '''
    return f"{COR_VERDE}{conteudo}{COR_BRANCA}"

def bright_vermelho(conteudo: Any) -> Any:
    '''
    Colore o texto informado em vermelho brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_VERMELHA}{conteudo}{COR_BRANCA}"

def limpar_console():
    '''
    Limpa o console de acordo com a plataforma.
    '''
    if platform.system() == 'Windows':
        os.system('cls')
    if platform.system() == 'Linux':
        os.system('clear')

def input_float(msg: str) -> float:
    '''
    Obtem número informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números são aceitos. Por favor, tente novamente.\n'))

def exibir_cabecalho() -> None:
    '''
    Exibe o cabeçalho.
    '''
    limpar_console()
    print(bright_amarelo('\n\t*****************************************************************'))
    print(bright_amarelo('\n\t** Calcular a soma, a subtração, a multiplicação e a divisão. **'))
    print(bright_amarelo('\n\t*****************************************************************\n'))

def obter_numero(numero: int) -> float:
    '''
    Obtem um número válido.
    Retorna o número.
    '''
    while True:
        numero_informado = input_float(f"\n\t{numero}° número: ")
        return numero_informado

def exibir_calculos(numeros: list[float]) -> None:
    '''
   Exibe os cáculos de soma, subtração, multiplicação e divisão no console.
    '''
    exibir_cabecalho()
    soma = numeros[0] + numeros[1]
    print(bright_amarelo("\tSoma"))
    print(bright_amarelo("\t****************"))
    print(f"\t{numeros[0]} + {numeros[1]} = {soma}")
    print(bright_amarelo("\t****************\n"))

    subtracao = numeros[0] - numeros[1]
    print(bright_amarelo("\tSubtração"))
    print(bright_amarelo("\t****************"))
    print(f"\t{numeros[0]} - {numeros[1]} = {subtracao}")
    print(bright_amarelo("\t****************\n"))

    multiplicacao = numeros[0] * numeros[1]
    print(bright_amarelo("\tMultiplicação"))
    print(bright_amarelo("\t****************"))
    print(f"\t{numeros[0]} x {numeros[1]} = {multiplicacao}")
    print(bright_amarelo("\t****************\n"))
 
    if numeros[1] == 0:
        print(bright_amarelo("\tDivisão"))
        print(bright_amarelo("\t*******************************************************"))
        print(bright_vermelho(f"\t{numeros[0]} / {numeros[1]} = Não é possível dividir por zero."))
        print(bright_amarelo("\t********************************************************\n"))
    else:
        divisao = numeros[0] / numeros[1]
        print(bright_amarelo("\tDivisão"))
        print(bright_amarelo("\t****************"))
        print(f"\t{numeros[0]} / {numeros[1]} = {divisao:.2f}")
        print(bright_amarelo("\t****************\n"))

def obter_numeros(qtd_numeros_informados: int = 2) -> list[float]:
    '''
     Obtem a quantidade de números inseridos pelo usuário na ordem ['1°', '2°'].
     Retorna uma lista com os números.
    '''
    numeros: list[float] = []
    for numero in range(1, qtd_numeros_informados+1):
        numero = obter_numero(numero)
        numeros.append(numero)
    return numeros

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    exibir_cabecalho()
    numero = obter_numeros()
    exibir_calculos(numero)


if __name__ == '__main__':
    main()
