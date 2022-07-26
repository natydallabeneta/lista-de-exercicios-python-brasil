"""
Exercício 10 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa receba dois vetores com mesmo tamanho. Gere um terceiro vetor com o dobro elementos, cujos valores
deverão ser compostos pelos elementos intercalados dos dois outros vetores.

    >>> intercalar([], [])
    []
    >>> intercalar([1],[2])
    [1, 2]
    >>> intercalar([1, 2], [3, 4])
    [1, 3, 2, 4]
    >>> intercalar(list(range(10)), list(range(10, 20)))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]

"""





def intercalar(lista_1: list, lista_2: list) -> list:
    """Escreva aqui em baixo a sua solução"""

    primeira_lista = lista_1
    segunda_lista = lista_2

    if not lista_1 and not lista_2:
        return []

    else:
        lista_intercalada = primeira_lista + segunda_lista   # juntar as duas listas em uma variante
        lista_intercalada[::2] = primeira_lista  # Substitui os itens da lista intercalada do início ao final de dois em dois, pelos itens da lista 1
        lista_intercalada[1::2] = segunda_lista  # Substitui os itens da lista intercalada do item 1 ao final de dois em dois, pelos itens da lista 2
        return lista_intercalada







