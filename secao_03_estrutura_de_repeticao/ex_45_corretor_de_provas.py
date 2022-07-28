"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""


def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""

    gabarito = ('A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A')

    total_alunos = 0
    total_notas = 0
    maior_nota = 0
    menor_nota = 10

    print('Aluno                 Nota')

# Desempacotamento dos dados
    for item in provas:
        total_alunos += 1
        nome = item[0]
        notas = item[1:]
        pontos = 0

# Contagem de pontos
        for i in range(0, len(gabarito)):
            if notas[i] == gabarito[i]:
                pontos += 1
        total_notas += pontos

        print(f'{nome}                 {pontos}')

# Maior e menor nota
        if maior_nota < pontos:
            maior_nota = pontos
        if menor_nota > pontos:
            menor_nota = pontos

    print('---------------------------')

# media
    media = total_notas / total_alunos

    print(f'Média geral: {media}')
    print(f'Maior nota: {maior_nota}')
    print(f'Menor nota: {menor_nota}')
    print(f'Total de Alunos: {total_alunos}')