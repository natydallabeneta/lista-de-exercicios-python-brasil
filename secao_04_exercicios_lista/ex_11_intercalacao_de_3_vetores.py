"""
Exercício 11 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Altere o programa anterior, intercalando 3 vetores.

    >>> intercalar([], [], [])
    []
    >>> intercalar([1], [2], [3])
    [1, 2, 3]
    >>> intercalar([1, 2], [3, 4], [5, 6])
    [1, 3, 5, 2, 4, 6]
    >>> intercalar(list(range(5)), list(range(5, 10)), list(range(10, 15)))
    [0, 5, 10, 1, 6, 11, 2, 7, 12, 3, 8, 13, 4, 9, 14]

"""


def intercalar(lista_1: list, lista_2: list, lista_3: list) -> list:
    """Escreva aqui em baixo a sua solução"""

    if not lista_1 and not lista_2 and not lista_3:
        return []

    if len(lista_1) and len(lista_2) and len(lista_3) == 1:
        return lista_1 + lista_2 + lista_3
    else:

        primeira_lista = lista_1
        segunda_lista = lista_2
        terceira_lista = lista_3

        lista_intercalada = primeira_lista + segunda_lista + terceira_lista
        lista_intercalada[::3] = primeira_lista
        lista_intercalada[1::3] = segunda_lista
        lista_intercalada[2::3] = terceira_lista

        return lista_intercalada
















