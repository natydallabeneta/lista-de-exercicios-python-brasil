"""
Exercício 14 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

    >>> calcular_qtde_numeros_pares_e_impares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    'Existem 5 números pares e 5 números impares'
    >>> calcular_qtde_numeros_pares_e_impares(12, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    'Existem 6 números pares e 4 números impares'
    >>> calcular_qtde_numeros_pares_e_impares(1, 1, 1, 1, 1, 1, 1, 1, 1,1)
    'Existem 0 números pares e 10 números impares'
    >>> calcular_qtde_numeros_pares_e_impares(2, 2, 2, 2, 2, 2, 2, 2, 2,2)
    'Existem 10 números pares e 0 números impares'

"""


def calcular_qtde_numeros_pares_e_impares(n1: int, n2: int, n3: int, n4: int, n5: int, n6: int, n7: int, n8: int, n9: int, n10: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    lista_de_numeros = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)
    numeros_pares = 0
    numeros_impares = 0

    for i in lista_de_numeros:
        if i % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1

    return f'Existem {numeros_pares} números pares e {numeros_impares} números impares'
