"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    """Escreva aqui em baixo a sua solução"""

    primeiro_numero = int(input('Digite o primeiro número inteiro: '))
    segundo_numero = int(input('Digite o segundo número inteiro: '))
    terceiro_numero = float(input('Digite um número real: '))

    dobro_do_primeiro_com_metade_segundo = round((primeiro_numero * 2) * (segundo_numero/2))
    triplo_do_primeiro_com_terceiro = primeiro_numero * 3 + terceiro_numero
    terceiro_elevado_ao_cubo = terceiro_numero ** 3

    print(f'O produto do dobro do primeiro com metade do segundo é {dobro_do_primeiro_com_metade_segundo:.2f}')
    print(f'A soma do triplo do primeiro com o terceiro é {triplo_do_primeiro_com_terceiro:.2f}')
    print(f'O terceiro elevado ao cubo é {terceiro_elevado_ao_cubo:.2f}')
