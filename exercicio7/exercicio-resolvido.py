'''
Solicite ao usuário o peso em kg e a altura em metros. 
Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
    IMC = peso / (altura x altura).
'''


import os
import platform
from typing import Final
from typing import Any

LINHA_TRACEJADA: Final[str] = '-' * 41
COR_BRANCA: Final[str] = '\033[0;0m'
COR_BRIGHT_AMARELA: Final[str] = '\033[93m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'


# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

def bright_amarelo(conteudo: Any) -> Any:
    '''
    Colore o texto informado em amarelo brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_AMARELA}{conteudo}{COR_BRANCA}"

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
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(bright_vermelho('\tApenas números são aceitos. Por favor, tente novamente.\n'))

def obter_peso() -> float:
    '''
    Obtem o peso do usuário.
    Retorna o peso válido.
    '''
    while True:
        peso = input_float('\n\tEntre com seu peso: ') 
        if 0 < peso < 300:
            return peso
        else:
           print(bright_vermelho('\tValor do peso inválido. Números negativos ou acima de 300 não são aceitos.')) 

def obter_altura() -> float:
    '''
    Obtem o altura do usuario.
    Retorna o altura válido.
    '''
    while True:
        altura = input_float('\n\tEntre com sua altura em metros: ') 
        if 0 < altura < 3.0:
            return altura
        else:
           print(bright_vermelho('\tValor da altura é inválido. Números negativos ou acima de 3.0 metros não são aceitos.'))

def calcular_indice_massa_corporal(peso: float, altura: float) -> float:
    '''
    Calcula o Índice de Massa Corporal (IMC) usando a fórmula:
    IMC = peso / (altura x altura).
    Retorna o indice.
    '''
    imc = peso / (altura * altura)     
    return imc
  
def exibir_classificacao_imc() -> None:
    '''
    Exibi a classificação do IMC.
    '''
    print('')
    print(f'\t{LINHA_TRACEJADA}')
    cabecalho = '\tInterpretação do IMC \n'
    print(f'\t{cabecalho}')
    print(f'\t{LINHA_TRACEJADA}')
    print('''
          ICM < 18.5 (Magreza)
          18.5 < ICM < 24.9 (Normal)
          25.0 < ICM < 29.9 (Sobrepeso)
          30.0 < ICM < 39.9 (Obseidade)
          ICM < 40.0 (Obsidade Grave)
        ''')
    print(f'\t{LINHA_TRACEJADA}')

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    exibir_classificacao_imc()
    print(bright_amarelo('\tInforme seu peso e altura e saiba seu IMC.\n'))
    peso = obter_peso()
    altura = obter_altura()
    resultado = calcular_indice_massa_corporal(peso, altura)
    print(bright_amarelo('\n\t........................ Resultado ..........................'))
    print(bright_amarelo(f"\n\tSeu IMC: {resultado:.2F}. Confira com a tabela acima a sua situação."))
    print(bright_amarelo('\n\t.............................................................'))

if __name__ == '__main__':
    main()
   