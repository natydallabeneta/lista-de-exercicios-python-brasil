"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""
from typing import Tuple, Any


def calcular_troco(valor: int) -> tuple[None, int] | tuple[str, int | Any]:
    """Escreva aqui em baixo a sua solução"""

    valor_do_saque = valor

    centenas_str = quinzenas_str = dezenas_str = cinco_str = unidades_str = ''

    if valor_do_saque > 600:
        return print("Valor indisponível")
    centenas_int, numero = divmod(valor_do_saque, 100)
    quinzenas_int, numero = divmod(numero, 50)
    dezenas_int, numero = divmod(numero, 10)
    cinco_int, numero = divmod(numero, 5)

    partes_numericas = 0
    # NOTAS DE 100
    if centenas_int == 1:
        centenas_str = f"{centenas_int} nota de R$ 100"
        partes_numericas += 1
    elif centenas_int > 1:
        centena_escrito = f'{centenas_int} notas de R$ 100'
        centenas_str = f'{centena_escrito}'
        partes_numericas += 1
    # NOTAS DE 50
    if quinzenas_int == 1:
        quinzenas_str = f"{quinzenas_int} nota de R$ 50"
        partes_numericas += 1
    # NOTAS DE 10

    if dezenas_int == 1:
        dezenas_str = f"{dezenas_int} nota de R$ 10"
        partes_numericas += 1

    elif dezenas_int > 1:
        dezena_escrito = f"{dezenas_int} notas de R$ 10"
        dezenas_str = f'{dezena_escrito}'
        partes_numericas += 1
    # NOTAS DE 5
    if cinco_int == 1:
        cinco_str = f"{cinco_int} nota de R$ 5"
        partes_numericas += 1

    if numero == 1:
        unidades_str = f'{numero} nota de R$ 1'
        partes_numericas += 1
    elif numero > 1:
        unidade_escrito = f'{numero} notas de R$ 1'

        unidades_str = f'{unidade_escrito}'
        partes_numericas += 1

    # IMPRESSÃO

    if partes_numericas == 1:
        print(f"'{centenas_str}{quinzenas_str}{dezenas_str}{unidades_str}{cinco_str}'")

    elif partes_numericas == 5:
        print(f"'{centenas_str}, {quinzenas_str}, {dezenas_str}, {cinco_str} e {unidades_str}'")

    elif partes_numericas == 4:
        if centenas_str == '':
            print(f"'{quinzenas_str}, {dezenas_str}, {cinco_str} e {unidades_str}'")
        elif quinzenas_str == '':
            print(f"'{centenas_str}, {dezenas_str}, {cinco_str} +  e + {unidades_str}'")
        elif dezenas_str == '':
            print(f"'{centenas_str}, {quinzenas_str}, {cinco_str} e {unidades_str}'")
        elif cinco_str == '':
            print(f"'{centenas_str}, {quinzenas_str}, {dezenas_str} e {unidades_str}'")
        else:
            print(f"'{centenas_str}, {quinzenas_str} , {dezenas_str} e {cinco_str}'")

    elif partes_numericas == 3:
        if centenas_str == '' and quinzenas_str == '':
            print(f"'{dezenas_str}, {cinco_str} e {unidades_str}'")
        elif quinzenas_str == '' and dezenas_str == '':
            print(f"'{centenas_str}, {cinco_str} e {unidades_str}'")
        elif dezenas_str == '' and cinco_str == '':
            print(f"'{centenas_str}, {quinzenas_str} e {unidades_str}'")
        elif cinco_str == '' and unidades_str == '':
            print(f"'{centenas_str}, {quinzenas_str} e {dezenas_str}'")
        elif unidades_str == '' and centenas_str == '':
            print(f'{quinzenas_str}, {dezenas_str} e {cinco_str}')

        elif centenas_str == '' and dezenas_str == '':
            print(f"'{quinzenas_str}, {cinco_str} e {unidades_str}'")
        elif centenas_str == '' and cinco_str == '':
            print(f"'{quinzenas_str}, {dezenas_str} e {unidades_str}'")

        elif quinzenas_str == '' and cinco_str == '':
            print(f"'{centenas_str}, {dezenas_str} e {unidades_str}'")
        elif quinzenas_str == '' and unidades_str == '':
            print(f"'{centenas_str}, {dezenas_str} e {cinco_str}'")

        elif dezenas_str == '' and unidades_str == '':
            print(f"'{centenas_str}, {quinzenas_str} e {cinco_str}'")
        elif dezenas_str == '' and centenas_str == '':
            print(f"'{quinzenas_str}, {cinco_str} e {unidades_str}'")

        elif cinco_str == '' and centenas_str == '':
            print(f"'{quinzenas_str}, {dezenas_str} e {unidades_str}'")
        elif cinco_str == '' and quinzenas_str == '':
            print(f"'{centenas_str}, {dezenas_str} e {unidades_str}'")

        elif unidades_str == '' and quinzenas_str == '':
            print(f"'{centenas_str}, {dezenas_str} e {cinco_str}'")
        elif unidades_str == '' and dezenas_str == '':
            print(f"'{centenas_str}, {quinzenas_str} e {cinco_str}'")


    elif partes_numericas == 2:
        if centenas_str == '' and quinzenas_str == '' and dezenas_str == '':
            print(f"'{cinco_str} e {unidades_str}'")
        elif centenas_str == '' and quinzenas_str == '' and cinco_str == '':
            print(f"'{dezenas_str} e {unidades_str}'")
        elif centenas_str == '' and quinzenas_str == '' and unidades_str == '':
            print(f"'{dezenas_str} e {cinco_str}'")

        elif quinzenas_str == '' and dezenas_str == '' and cinco_str == '':
            print(f"'{centenas_str} e {unidades_str}'")
        elif quinzenas_str == '' and dezenas_str == '' and unidades_str == '':
            print(f"'{centenas_str} e {cinco_str}'")


        elif dezenas_str == '' and cinco_str == '' and unidades_str == '':
            print(f"'{centenas_str} e {quinzenas_str}'")
        elif dezenas_str == '' and cinco_str == '' and centenas_str == '':
            print(f"'{quinzenas_str} e {unidades_str}'")

        elif cinco_str == '' and unidades_str == '' and centenas_str == '':
            print(f"'{quinzenas_str} e {dezenas_str} '")
        elif cinco_str == '' and unidades_str == '' and quinzenas_str == '':
            print(f"'{centenas_str} e {dezenas_str}'")
