"""
Exercício 28 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

Mostre os valores monetórios com duas casas decimais..

    >>> import ex_28_colecao_de_cds
    >>> entradas = ['1', '1']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 1
    Valor total da coleção: R$ 1.00
    Custo médio dos cds: R$ 1.00
    >>> entradas = ['40', '40', '2']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 2
    Valor total da coleção: R$ 80.00
    Custo médio dos cds: R$ 40.00
    >>> entradas = ['10', '20', '30', '40', '4']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 4
    Valor total da coleção: R$ 100.00
    Custo médio dos cds: R$ 25.00
    >>> entradas = ['10', '20', '30', '3']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 3
    Valor total da coleção: R$ 60.00
    Custo médio dos cds: R$ 20.00

"""


def calcular_estatisticas_colecao_de_cd():
    """Escreva aqui em baixo a sua solução"""

    quantidade_cds = int(input('Informe a quantidade de CDs: '))
    total_cds = 0
    valores = []
    soma = 0
    media = 0

    while total_cds != quantidade_cds:
        valor_por_cd = float(input('Digite o valor para em cada CD. R$: '))
        valores.append(valor_por_cd)
        total_cds += 1

    for valor in valores:
        soma += valor
        media = soma / quantidade_cds



    print(f'Número de cds: {quantidade_cds}')
    print(f'Valor total da coleção: R$ {soma:.2f}')
    print(f'Custo médio dos cds: R$ {media:.2f}')
