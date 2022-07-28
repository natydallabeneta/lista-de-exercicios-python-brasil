"""
Exercício 06 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0, e imprima separado o número de alunos com nota menor que 7.0 .

    >>> calcular_media([8,9,10,2],[2,10,9,5],[5,2,9,10],[10,1,1,10],[9,2,9,8],[8,8,9,7],[7,7,7,9],[4,6,5,7],[1,2,8,10],[10,2,2,8])
    Alunos com media >= 7.0: 4
    Alunos com media < 7.0: 6
    >>> calcular_media([2,1,1,2],[2,1,0,4],[3,2,5,2],[9,7,7,9],[0,6,9,2],[9,1,6,4],[10,10,9,7],[6,7,8,9],[9,8,9,6],[10,5,10,8])
    Alunos com media >= 7.0: 5
    Alunos com media < 7.0: 5
"""


def calcular_media(*notas) -> int:
    """Escreva aqui em baixo a sua solução"""

    maior_7 = 0
    menor_7 = 0

    for item in notas:
        total_notas_por_aluno = len(item)
        soma_das_notas = 0

        for i in item:
            soma_das_notas += i
        media = soma_das_notas/total_notas_por_aluno

        if media >= 7:
            maior_7 += 1
        else:
            menor_7 += 1

    print(f'Alunos com media >= 7.0: {maior_7}')
    print(f'Alunos com media < 7.0: {menor_7}')
