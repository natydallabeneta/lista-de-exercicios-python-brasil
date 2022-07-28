"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""

    # MAIOR E MENOR INDICE COM NOME DA CIDADE
    maior_indice_de_acidentes = 0
    nome_da_cidade_com_maior_indice = ''
    menor_indice_de_acidentes = 10
    nome_da_cidade_com_menor_indice = ''

    # MEDIA GERAL
    total_de_veiculos = 0

    # MÉDIAS PARA CIDADES COM MENOS DE 150_000 CARROS
    total_cidades_menos_150 = 0
    total_de_acidentes_menos_150 = 0

    # UTILIZAR O FOR PARA DESEMPACOTAR OS VALORES
    for item in cidades:
        nome = item[0]
        numero_de_veiculos = item[1]
        numero_de_acidentes = item[2]
        total_de_veiculos += numero_de_veiculos
        indice_acidente = (numero_de_acidentes / numero_de_veiculos) * 1000

    # ENCONTRAR O MAIOR E MENOR INDICE DE ACIDENTE
        if maior_indice_de_acidentes < indice_acidente:
            maior_indice_de_acidentes = indice_acidente
            nome_da_cidade_com_maior_indice = nome

        if indice_acidente < menor_indice_de_acidentes:
            menor_indice_de_acidentes = indice_acidente
            nome_da_cidade_com_menor_indice = nome

    # DADOS PARA CIDADES COM MENOS DE 150_000 CARROS
        if numero_de_veiculos <= 150000:
            total_cidades_menos_150 += 1
            total_de_acidentes_menos_150 += numero_de_acidentes

    media_de_veiculos = total_de_veiculos / len(cidades)
    media_menos_150 = total_de_acidentes_menos_150 / total_cidades_menos_150

    print(f'O maior índice de acidentes é de {nome_da_cidade_com_maior_indice}, com {maior_indice_de_acidentes:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {nome_da_cidade_com_menor_indice}, com {menor_indice_de_acidentes:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {int(media_de_veiculos)}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_menos_150} acidentes.')
