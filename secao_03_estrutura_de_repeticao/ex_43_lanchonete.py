"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""


def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""

    # VARIANTES
    valor_final = 0
    total_itens_pedido = 0
    pedido = {}

    # PRINT CABEÇALHO
    print('_____________________________________________________________________________')
    print('|                              RESUMO DA CONTA                              |')
    print('|---------------------------------------------------------------------------|')
    print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')

    # PRINT FUNÇÃO VAZIA
    if not itens:
        print('|---------------------------------------------------------------------------|')
        print('| Total Geral:                                    |          0 |       0.00 |')
        print('-----------------------------------------------------------------------------')

    # COLOCAR OS ITENS EM UM DICIONÁRIO PARA TOTALIZAR A QUANTIDADE DE ITEM
    for item in itens:
        chave = item[0]
        valor = item[1]
        if chave in pedido:
            pedido[chave] += valor
            total_itens_pedido += valor
        else:
            pedido[chave] = valor
            total_itens_pedido += valor

    # VALOR POR ITENS
    for chave, valor in pedido.items():
        if chave == '100':
            lanche = 'Cachorro Quente'
            quantidade = valor
            valor_lanche = 1.20
            total_pedido = valor_lanche * quantidade
            valor_final += total_pedido

        if chave == '101':
            lanche = 'Bauru Simples'
            quantidade = valor
            valor_lanche = 1.30
            total_pedido = valor_lanche * quantidade
            valor_final += total_pedido

        if chave == '102':
            lanche = 'Bauru com Ovo'
            quantidade = valor
            valor_lanche = 1.50
            total_pedido = valor_lanche * quantidade
            valor_final += total_pedido

        if chave == '103':
            lanche = 'Hamburger'
            quantidade = valor
            valor_lanche = 1.20
            total_pedido = valor_lanche * quantidade
            valor_final += total_pedido

        if chave == '104':
            lanche = 'Cheeseburger'
            quantidade = valor
            valor_lanche = 1.30
            total_pedido = valor_lanche * quantidade
            valor_final += total_pedido

        if chave == '105':
            lanche = 'Refrigerante'
            quantidade = valor
            valor_lanche = 1.0
            total_pedido = valor_lanche * quantidade
            valor_final += total_pedido

        print('| ', end='')
        print(f'{lanche:<15}', end='  | ')
        print(f'{chave:.8}', end='    | ')
        print(f'{valor_lanche:.2f}', end='                |')
        print(f' {quantidade:>10} ', end='|       ')
        print(f'{quantidade * valor_lanche:.2f} |')

    if len(itens) == 1:
        print('|---------------------------------------------------------------------------|')
        print(
        f'| Total Geral:                                    |          {valor} |       {valor_lanche:.2f} |')
        print('-----------------------------------------------------------------------------')

    if len(itens) > 1:
        print('|---------------------------------------------------------------------------|')
        print(f'| Total Geral:                                    |{total_itens_pedido:11} | {valor_final:10.2f} |')
        print('-----------------------------------------------------------------------------')

