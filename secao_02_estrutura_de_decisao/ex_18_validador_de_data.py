"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    try:
        dia, mes, ano = map(int, data.split('/'))
    except:
        print("'Data inválida'")
    else:
        valida = False

        dia, mes, ano = map(int, data.split('/'))
        valida = False


        # Meses com 31 dias
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if 1 >= dia <= 31:
                valida = True

        # Meses com 30 dias
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia <= 30:
                valida = True

        # se o mês for fevereiro, precisamos saber se ele é Bissexto
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia <= 29:
                    valida = True
            elif dia <= 28:
                valida = True

        if valida:
            print("'Data válida'")
        else:
            print("'Data inválida'")