"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x, y, z):
    """Escreva aqui em baixo a sua solução"""

    primeiro = x
    segundo = y
    terceiro = z

    if terceiro > segundo:
        aux = terceiro
        terceiro = segundo
        segundo = aux

    if segundo > primeiro:
        aux = segundo
        segundo = primeiro
        primeiro = aux

    if terceiro > primeiro:
        aux = terceiro
        terceiro = primeiro
        primeiro = aux

    if terceiro > segundo:
        aux = terceiro
        terceiro = segundo
        segundo = aux

    print(f'{primeiro}, {segundo}, {terceiro}')

ordenar_decrescente(2, 3, 5)