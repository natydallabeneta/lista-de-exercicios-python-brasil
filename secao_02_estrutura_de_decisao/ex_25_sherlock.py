"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investivar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investivar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investivar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investivar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investivar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investivar('Não','Não','Não','Não','Não')
    'Inocente'

"""


def investivar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):
    """Escreva aqui em baixo a sua solução"""

    respostas = [telefonou, estava_no_local, mora_perto, devia, trabalhou]
    contador = 0

    for resposta in respostas:
        if resposta == 'Sim':
            contador += 1

    if contador >= 5:
        print("'Assassino'")
    elif contador >= 3:
        print("'Cúmplice'")
    elif contador >= 2:
        print("'Suspeito'")
    else:
        print("'Inocente'")
