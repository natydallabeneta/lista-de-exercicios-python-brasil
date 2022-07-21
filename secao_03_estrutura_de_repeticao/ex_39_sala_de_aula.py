"""
Exercício 39 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais alto
 e o número do aluno mais baixo, junto com suas alturas.
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162))
    'O maior aluno é o Renzo com 162 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165))
    'O maior aluno é o Clara com 165 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))
    'O maior aluno é o Oscar com 199 cm. O menor aluno é o Renzo com 162 cm'

"""


def calcular_aluno_mais_baixo_e_mais_alto(*alunos) -> str:
    """Escreva aqui em baixo a sua solução"""

    maior_altura = 0
    menor_altura = 999
    aluno_mais_alto = None
    aluno_mais_baixo = None

    if len(alunos) == 1:
        return f'O maior aluno é o {alunos[0][0]} com {alunos[0][1]} cm. O menor aluno é o {alunos[0][0]} com {alunos[0][1]} cm'
    else:
        for item in alunos:
            if item[1] > maior_altura:
                maior_altura = item[1]
                aluno_mais_alto = item[0]
            if item[1] < menor_altura:
                menor_altura = item[1]
                aluno_mais_baixo = item[0]

    return f'O maior aluno é o {aluno_mais_alto} com {maior_altura} cm. O menor aluno é o {aluno_mais_baixo} com {menor_altura} cm'
