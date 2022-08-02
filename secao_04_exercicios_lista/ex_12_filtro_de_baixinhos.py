"""
Exercício 12 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Foram anotados os nomes, as idades e alturas de de vários alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses
alunos.

Mostre a média com uma casa decimal.

    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162))
    Média de altura: 162.0 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158))
    Média de altura: 160.0 centímetros.
    Existe(m) 1 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210))
    Média de altura: 176.7 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210), ('Criança', 7, 100)
    ... )
    Média de altura: 157.5 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210),
    ...     ('Criança', 7, 100), ("Shaquille O'Neal", 25, 216)
    ... )
    Média de altura: 169.2 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade

"""


def calcular_baixinhos_com_mais_de_13_anos(*alunos):
    """Escreva aqui em baixo a sua solução"""

    soma_altura = 0
    aluno_abaixo_da_media = 0
    lista_altura = []
    lista_alunos_maior_13 = []
    lista_de_alunos_abaixo_media = []

# Desempacotando dados para calculo da media
    for item in alunos:
        idade = item[1]
        altura = float(item[2])
        lista_altura.append(altura)
        soma_altura += altura
        if idade > 13:
            lista_alunos_maior_13.append(item)

    media = soma_altura / len(alunos)
    print(f'Média de altura: {media:.1f} centímetros.')

# Alunos com mais de 13 anos, abaixo da altura média
    for item in lista_alunos_maior_13:
        altura = float(item[2])

        if altura < media:
            aluno_abaixo_da_media += 1
            lista_de_alunos_abaixo_media.append(item)

    if aluno_abaixo_da_media >= 1:
        print(f'Existe(m) {aluno_abaixo_da_media} aluno(s) com altura abaixo da média com mais de 13 anos:')
    else:
        print('Não há nenhum aluno abaixo da média')

    for item, dados in enumerate(lista_de_alunos_abaixo_media, start=1):
        nome, idade, altura = dados
        print(f'{item}. {nome}, com {altura} centímetros e {idade} ano(s) de idade')
