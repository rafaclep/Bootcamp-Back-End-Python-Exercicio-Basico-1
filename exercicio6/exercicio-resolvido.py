'''
Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
'''


import os
import platform
import math
from typing import Final
from typing import Any

LINHA_TRACEJADA: Final[str] = '-' * 31
COR_BRANCA: Final[str] = '\033[0;0m'
COR_VERDE: Final[str] = '\033[32m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'
OPCOES_DE_TRANSPORTE:  Final[dict[str, str ]] = {
    'A': 'Avião',
    'O': 'Ônibus',
    'C': 'Carro',    
}

# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

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
        print(f"\n\t'{bright_vermelho(opcao)}' é uma opção inválida! As opções válidas são: {verde(', '.join(opcoes))}") # pylint: disable=line-too-long

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
    cabecalho = 'MENU DE OPÇÕES \n'
    print(verde(cabecalho.center(50)))


    for key, value in opcoes.items():
        opcao = '|' + key + '|' + "  "  + value
        print(f"\t\t{verde(opcao)} ")
    print(verde(f'\t{LINHA_TRACEJADA}'))

def obter_quilometro() -> float:
    '''
    Obtem os quilômetros informados pelo usuário.
    Retorna os quilômetros válidos.
    '''
    while True:
        quilometros_informados =  input_float('\tDistância em Km: ')
        if quilometros_informados > 0:
            return quilometros_informados
        print(bright_vermelho('\tValor do quilômetro inválido. Entre com um valor acima de zero.'))

def calcular_tempo_de_viagem(distancia: float, velocidade: float) -> float:
    '''
    Calcula o tempo de viagem gasto.
    '''
    tempo_de_viagem = distancia / velocidade
    return tempo_de_viagem

def passar_para_texto(valor) -> str:
    '''
    Recebe um número e passa texto.
    '''
    inteiro = math.trunc(valor)
    fracionado = valor - inteiro
    minutos = math.trunc(fracionado * 60)
    return f"{inteiro} horas e {minutos} minutos"

def calcular_tempo_da_viagem_de_aviao(distancia: float) -> float:
    '''
    Calcula o tempo de viagem de avião - distancia(km)
    '''
    velocidade_do_aviao = 600
    return calcular_tempo_de_viagem(distancia, velocidade_do_aviao)

def calcular_tempo_da_viagem_de_carro(distancia: float) -> float:
    '''
    Calcula o tempo de viagem de carro - distancia(km)
    '''
    velocidade_do_carro = 100
    return calcular_tempo_de_viagem(distancia, velocidade_do_carro)

def calcular_tempo_da_viagem_de_onibus(distancia: float) -> float:
    '''
    Calcula o tempo de viagem de carro - distancia(km)
    '''
    velocidade_do_onibus = 80
    return calcular_tempo_de_viagem(distancia, velocidade_do_onibus)

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    print(verde('\tSaiba quanto tempo sua viagem vai levar.\n'))
    while True:
        exibir_menu(OPCOES_DE_TRANSPORTE)
        transporte = input_opcoes('\tTipo de transporte: ', OPCOES_DE_TRANSPORTE)
        distancia = obter_quilometro()
        if transporte == 'A':
            tempo_de_viagem = calcular_tempo_da_viagem_de_aviao(distancia)
            tempo_formatado = passar_para_texto(tempo_de_viagem)
            print(f'\n\tTempo estimado de viagem {tempo_formatado}')

        elif transporte == 'O':
            tempo_de_viagem = calcular_tempo_da_viagem_de_onibus(distancia)
            tempo_formatado = passar_para_texto(tempo_de_viagem)
            print(f'\n\tTempo estimado de viagem {tempo_formatado}')

        elif transporte == 'C':
            tempo_de_viagem = calcular_tempo_da_viagem_de_carro(distancia)
            tempo_formatado = passar_para_texto(tempo_de_viagem)
            print(f'\n\tTempo estimado de viagem {tempo_formatado}')
        break

if __name__ == '__main__':
    main()