'''
exercício 5 do Desafio_1 - Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de Renda.
    ● Renda até R$ 1.903,98: isento de imposto de renda;
    ● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
    ● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
    ● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
    ● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''
import locale
import os
import platform
from typing import Final
from typing import Any
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

LINHA_ASTERISCO: Final[str] = '*' * 68
COR_BRANCA: Final[str] = '\033[0;0m'
COR_VERDE: Final[str] = '\033[32m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'

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

def limpar_console():
    '''
    Limpa o console de acordo com a plataforma.
    '''
    if platform.system() == 'Windows':
        os.system('cls')
    if platform.system() == 'Linux':
        os.system('clear')

def exibir_valores_de_percentual_imposto_de_renda() -> None:
    '''
    Exibi os valores das alíquotas de imposto de renda de acordo com a faixa salarial.
    '''
    print(verde(f'\t{LINHA_ASTERISCO}'))
    print(verde('''
            \tRenda até R$ 1.903,98: isento de imposto de renda;
            \n\t\tRenda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%; 
            \n\t\tRenda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
            \n\t\tRenda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
            \n\t\tRenda acima de R$ 4.664,68: alíquota máxima de 27,5%.
        '''))
    print(verde(f'\t{LINHA_ASTERISCO}'))

def formatar_valor_monetario(valor:float) -> str:
    '''
    Formata valor para  moeda brasileira.
    '''
    moeda_formatada = locale.currency(valor, grouping=True)
    return moeda_formatada

def obter_renda() -> float:
    '''
    Obtem o valor da renda iformado pelo usuário.
    Retorna o valor da renda válido.
    '''
    while True:
        renda_informada =  input_float('\tRenda bruta R$: ')
        if renda_informada > 0:
            return renda_informada
        print(bright_vermelho('\tValor da renda inválida. Entre com um valor acima de zero.'))

def calcular_salario_liquido(renda: float, percentual: float) -> float:
    '''
    Calcula o salário liquido.
    Retorna o salário.
    '''
    calculo = percentual * renda
    imposto = calculo / 100
    salario_liquido =   renda - imposto
    return salario_liquido

def calcular_salario_liquido_por_faixa_salarial (renda: float ) -> float:
    '''
    Calcula o salário liquido de acordo com a faixa salarial. 
    Retorna o salário.
    '''
    if 1_903.98 <= renda <= 2_826.65:
        salario_liquido = calcular_salario_liquido(renda, 7.5)
        return salario_liquido
    if 2_826.66 <= renda <=  3_751.05:
        salario_liquido = calcular_salario_liquido(renda, 15)
        return salario_liquido
    if 3_751.06 <= renda <= 4_664.68:
        salario_liquido = calcular_salario_liquido(renda, 22.5)
        return salario_liquido
    if renda > 4_664.68:
        salario_liquido = calcular_salario_liquido(renda, 27.5)
        return salario_liquido
    return renda

def main() -> None:
    '''
    Fluxo principal do programa.
    '''
    limpar_console()
    exibir_valores_de_percentual_imposto_de_renda()
    print('\n\t***  Informe sua renda bruta para saber seu salário liquido.  ***\n')
    renda_informada = obter_renda()
    resultado = calcular_salario_liquido_por_faixa_salarial(renda_informada)
    print(verde('\n\t............... Resultado ....................'))
    print(f"\n\t\tSeu salário líquido é {formatar_valor_monetario(resultado)}")
    print(verde('\n\t..............................................'))

if __name__ == '__main__':
    main()