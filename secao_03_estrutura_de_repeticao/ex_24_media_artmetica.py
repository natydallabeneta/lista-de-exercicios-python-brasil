"""
Exercício 24 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o mostre a média aritmética de N notas.

    >>> calcular_media()
    'É necessária ao menos uma nota para calcular a média'
    >>> calcular_media(1)
    1.0
    >>> calcular_media(1, 3)
    2.0
    >>> calcular_media(1, 3, 3)
    2.3333333333333335

"""


def calcular_media(*notas) -> float:
    """Escreva aqui em baixo a sua solução"""

    total = 0
    if not notas:
        return 'É necessária ao menos uma nota para calcular a média'
    for i in notas:
        total += i
    media = total/len(notas)
    return media
