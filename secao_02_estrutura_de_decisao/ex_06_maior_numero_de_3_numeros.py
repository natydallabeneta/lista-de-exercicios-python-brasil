"""
Exercício 06 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    5
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    -1
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    3
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    15
"""


def calcular_maior_de_3_numeros(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    maior = 0

    if x > y and x > z:
        maior = x
    elif y > x and y > z:
        maior = y
    elif z > x and z > y:
        maior = z

    print(f'{maior}')