"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Faça um programa para imprimir:

  1
  2   2
  3   3   3
  .....
  n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

"""


def piramide(n):
    for linha in range(n+1):
        for coluna in range(0, linha):
            print(linha, end=' ')
        print('')

