"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True
"""
from typing import Tuple


def calcular_primos_e_divisoes(n: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""

    retorno_2 = 0
    retorno_1 = []
    # Passa por todos os números até o limite superior definido pelo usuario
    # Para cada número, vai testar se ele é primo
    # No teste não é considerado como 'divisoes' quando um número é divido por 1 e por dois, por isso o contador do
    # código inicia em -2.

    for numero in range(2, n + 1):

        contador = 0
        divisoes = -2

        if numero >= 2:
            for divisor in range(1, numero + 1):
                divisoes += 1
                if numero % divisor == 0:
                    contador += 1
        if contador == 2:
            retorno_1.append(str(numero))
            retorno_2 += divisoes
        else:
            retorno_2 += divisoes

    retorno = [', '.join(retorno_1), retorno_2]
    return retorno
