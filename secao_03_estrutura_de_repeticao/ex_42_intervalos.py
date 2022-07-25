"""
Exercício 42 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

    >>> import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-1, 10, 15, 20, 50, 13, 78, 22, 14, 16]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    7 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> import  ex_42_intervalos
    >>> numeros_para_avaliacao=[14, -5, 10, 2, 80, 99]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    2 número(s) entre o intervalo de zero a 25
    2 número(s) entre o intervalo de 76 a 100
    >>> import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-55, 144, 5, 32, 18, 43, 12, 26, 76]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    3 número(s) entre o intervalo de zero a 25
    3 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> import  ex_42_intervalos
    >>> numeros_para_avaliacao=[3, 5, 100, -5, 70, 88, 28, 12]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    1 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 51 a 75
    1 número(s) entre o intervalo de 76 a 100

"""


def listar_numeros_para_avaliacao():
    """Escreva aqui em baixo a sua solução"""

    numeros_para_avaliacao = 0
    intervalo_de_zero_a_25 = 0
    intervalo_de_26_a_50 = 0
    intervalo_de_51_a_75 = 0
    intervalo_de_76_a_100 = 0

    while numeros_para_avaliacao >= 0:
        numeros_para_avaliacao = int(input('Digite um número: '))
        if 0 <= numeros_para_avaliacao <= 25:
            intervalo_de_zero_a_25 += 1
        elif 26 <= numeros_para_avaliacao <= 50:
            intervalo_de_26_a_50 += 1
        elif 51 <= numeros_para_avaliacao <= 75:
            intervalo_de_51_a_75 += 1
        elif 76 <= numeros_para_avaliacao <= 100:
            intervalo_de_76_a_100 += 1

    # print
    if intervalo_de_zero_a_25 >= 1:
        print(f'{intervalo_de_zero_a_25} número(s) entre o intervalo de zero a 25')
    if intervalo_de_26_a_50 >= 1:
        print(f'{intervalo_de_26_a_50} número(s) entre o intervalo de 26 a 50')
    if intervalo_de_51_a_75 >= 1:
        print(f'{intervalo_de_51_a_75} número(s) entre o intervalo de 51 a 75')
    if intervalo_de_76_a_100 >= 1:
        print(f'{intervalo_de_76_a_100} número(s) entre o intervalo de 76 a 100')
