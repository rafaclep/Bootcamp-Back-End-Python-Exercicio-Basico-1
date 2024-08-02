'''
exercício 1 do Desafio_1 - Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão.
'''

import os
import re
import platform
from typing import Final
from typing import Any

LINHA_TRACEJADA: Final[str] = '-' * 31
COR_BRANCA: Final[str] = '\033[0;0m'
COR_BRIGHT_AMARELA: Final[str] = '\033[93m'
COR_VERDE: Final[str] = '\033[32m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'
OPERADORES_E_TERMOS:  Final[dict[str, str ]] = {
    '+': 'Soma',
    '-': 'Subtração',
    '*': 'Multiplicação',
    '/': 'Divisão'
}
VALIDACAO_DA_FORMULA: Final[str] = r'^\s*\d{1,8}(?:\.\d{1,2}|)\s*[*+-/]\s*\d{1,8}(?:\.\d{1,2}|)\s*$'

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

def input_opcoes(msg: str, opcoes: dict[str, str ]) -> str:
    '''
    Obtem a opção válida.
    Retorna a opção.
    '''
    while True:
        opcao = input(msg).upper()
        if opcao in opcoes:
            return opcao
        print(f"'{bright_vermelho(opcao)}'\tOpção inválida! As opções válidas são: {verde(', '.join(opcoes))}") # pylint: disable=line-too-long

def input_int(msg: str) -> int:
    '''
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números inteiros são aceitos. Por favor, tente novamente.\n'))

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

def exibir_menu(opcoes: dict[str, str]) -> None:
    '''
    Exibi o menu de opções.
    '''
    print('')
    print(verde(f'\t{LINHA_TRACEJADA}'))
    cabecalho = 'MENU DE OPÇÕES PARA O CÁLCULO\n'
    print(verde(cabecalho.center(50)))


    for key, value in opcoes.items():
        opcao = '|' + key + '|' + "  "  + value
        print(f"\t\t{verde(opcao)} ")
    print(verde(f'\t{LINHA_TRACEJADA}'))

def calcular_operacoes(calculo:str) -> float:
    '''
    Calcula a operação aritmética de acordo com o operador e os numeros informadas pelo usuário.
    Retorna o resultado da operação.
    '''
    if '*' in calculo:
        numero_1, numero_2 = calculo.split("*")
        return float(numero_1) * float(numero_2)
    elif '/' in calculo:
        numero_1, numero_2 = calculo.split("/")
        return float(numero_1) / float(numero_2)
    elif '-' in calculo:
        numero_1, numero_2 = calculo.split("-")
        return float(numero_1) - float(numero_2)
    elif '+' in calculo:
        numero_1, numero_2 = calculo.split("+")
        return float(numero_1) + float(numero_2)
    raise ValueError(bright_vermelho(f'\tNão é possível realizar cálculo para o operador = {calculo}'))


def input_calculo() -> str:
    '''
    Obtem as entrada para o calculo.
    Retorna o calculo.
    '''
    while True:
        calculo = input("\tCalcular: ")
        calculo_valido = re.match(VALIDACAO_DA_FORMULA, calculo)
        if calculo_valido:
            return calculo
        print(bright_vermelho(f'\tNão é possível realizar cálculo {calculo}. Por favor, tente novamente.'))


def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    print(verde('\t\tFaça seu cálculo.'))
    exibir_menu(OPERADORES_E_TERMOS)
    calculo = input_calculo()
    limpar_console()
    print(bright_amarelo(f"\n\t O resultado de {calculo} é: {calcular_operacoes(calculo):.2f}"))

if __name__ == '__main__':
    main()