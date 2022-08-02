"""
Exercício 13 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule e MOSTRE A MÉDIA ANUAL das temperaturas e MOSTRE TODAS AS TEMPERATURAS ACIMA DA MÉDIA ANUAL,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

-as temperaturas só serão dadas em inteiro
-todos os meses do ano serão passados à funçao, começando de janeiro e terminando em dezembro.
 Todos seguidos de sua temperatura mensal

(Funçoês recomendadas para estudo:
    - .ljust()
    - enumerate()
    - sum()
    - len()


    >>> import ex_13_media_de_temperaturas_anual

    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '30']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 24.75 Graus
     1 - Janeiro:       30°
     2 - Fevereiro:     33°
     3 - Março:         27°
     4 - Abril:         25°
     5 - Maio:          29°
     6 - Junho:         25°
    11 - Novembro:      33°
    12 - Dezembro:      25°
    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '35']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 25.17 Graus
     1 - Janeiro:       35°
     2 - Fevereiro:     33°
     3 - Março:         27°
     5 - Maio:          29°
    11 - Novembro:      33°

"""


def temperaturas_acima_da_media():
    """Escreva aqui sua solução: """

# Criar uma variável com os meses do ano e uma variável vazia para adicionar as temperaturas:
    meses = ["Janeiro:", "Fevereiro:", "Março:", "Abril:", "Maio:", "Junho:", "Julho:", "Agosto:", "Setembro:",
             "Outubro:", "Novembro:", "Dezembro:"]

    meses_vs_temperaturas = []

# Fazer um "for" para solicitar os inputs da temperatua e no input utilizar uma "f'string" para ligar o mês com o valor
# da temperatura e adicionar os valores na variável vazia.

    for i in range(12):
        meses_vs_temperaturas.append(int(input(f'Digite a media de temperatura de {meses[i]} : ')))

    media = sum(meses_vs_temperaturas)/12
    print(f'Média anual: {media:.2f} Graus')

# Imprimir os dados conforme os indices
    for i in range(12):
        if meses_vs_temperaturas[i] > media:
            print(f"{i+1:>2} - {meses[i]:<14} {meses_vs_temperaturas[i]}°")
