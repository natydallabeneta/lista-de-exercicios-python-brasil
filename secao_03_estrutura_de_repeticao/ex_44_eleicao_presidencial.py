"""
Exercício 44 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


    >>> apurar_votos('1')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1     100.0%
    2                   Luladrão          0       0.0%
    3                   Dilmanta          0       0.0%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      50.0%
    2                   Luladrão          1      50.0%
    3                   Dilmanta          0       0.0%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      33.3%
    2                   Luladrão          1      33.3%
    3                   Dilmanta          1      33.3%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      25.0%
    2                   Luladrão          1      25.0%
    3                   Dilmanta          1      25.0%
    4                   FHC Isentão       1      25.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      20.0%
    2                   Luladrão          1      20.0%
    3                   Dilmanta          1      20.0%
    4                   FHC Isentão       1      20.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      20.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      16.7%
    2                   Luladrão          1      16.7%
    3                   Dilmanta          1      16.7%
    4                   FHC Isentão       1      16.7%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      16.7%
    6                   Votos Brancos     1      16.7%
    >>> apurar_votos('1', '2', '3', '4', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1       5.6%
    2                   Luladrão          1       5.6%
    3                   Dilmanta          1       5.6%
    4                   FHC Isentão       1       5.6%
    -------------------------------------------------------------------
    5                   Votos Nulos       7      38.9%
    6                   Votos Brancos     7      38.9%


"""
from collections import Counter


def apurar_votos(*votos):
    """Escreva aqui em baixo a sua solução"""

    bostonaro = 0
    luladrao = 0
    silmanta = 0
    isentao = 0
    votos_nnulos = 0
    votos_brancos = 0
    total_votos = len(votos)

# contagem de votos
    for i in votos:
        if i == '1':
            bostonaro += 1
        if i == '2':
            luladrao += 1
        if i == '3':
            silmanta += 1
        if i == '4':
            isentao += 1
        if i == '5':
            votos_nnulos += 1
        if i == '6':
            votos_brancos += 1

    print('Código do Candidato Nome do Candidato Votos Porcentagem sobre total')
    print(f'1                   Bostonaro         {bostonaro}{100/total_votos*bostonaro:10.1f}%')
    print(f'2                   Luladrão          {luladrao}{100/total_votos*luladrao:10.1f}%')
    print(f'3                   Dilmanta          {silmanta}{100/total_votos*silmanta:10.1f}%')
    print(f'4                   FHC Isentão       {isentao}{100/total_votos*isentao:10.1f}%')
    print(f'-------------------------------------------------------------------')
    print(f'5                   Votos Nulos       {votos_nnulos}{100/total_votos*votos_nnulos:10.1f}%')
    print(f'6                   Votos Brancos     {votos_brancos}{100/total_votos*votos_brancos:10.1f}%')
