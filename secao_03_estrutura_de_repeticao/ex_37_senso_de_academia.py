"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""

    # Solicitar primeiro input antes de entrar no while
    nome = input('Digite o seu nome: ')
    altura = int(input('Digite a sua altura: '))
    peso = int(input('Digite o seu peso: '))

    # Armazenar dados de peso e altura
    mais_alto = [nome, altura]
    mais_baixo = [nome, altura]
    mais_magro = [nome, peso]
    mais_gordo = [nome, peso]

    # Calcular média dos dados
    total_de_pessoas = 1
    total_de_alturas = altura
    total_de_peso = peso
    media_altura = float(total_de_alturas / total_de_pessoas)
    media_peso = float(total_de_peso / total_de_pessoas)

    while not nome == '0':
        nome = input('Digite o seu nome: ')

        if nome == '0':
            print(f'Cliente mais alto: {mais_alto[0]}, com {mais_alto[1]} centímetros')
            print(f'Cliente mais baixo: {mais_baixo[0]}, com {mais_baixo[1]} centímetros')
            print(f'Cliente mais magro: {mais_magro[0]}, com {mais_magro[1]} kilos')
            print(f'Cliente mais gordo: {mais_gordo[0]}, com {mais_gordo[1]} kilos')
            print('--------------------------------------------------')
            print(f'Media de altura dos clientes: {media_altura:.1f} centímetros')
            print(f'Media de peso dos clientes: {media_peso:.1f} kilos')
        else:
            total_de_pessoas += 1
            altura = int(input('Digite a sua altura: '))
            total_de_alturas += altura
            media_altura = total_de_alturas / total_de_pessoas
            peso = int(input('Digite o seu peso: '))
            total_de_peso += peso
            media_peso = float(total_de_peso / total_de_pessoas)

            if mais_alto[1] < altura:
                mais_alto = [nome, altura]
            if altura < mais_baixo[1]:
                mais_baixo = [nome, altura]
            if mais_gordo[1] < peso:
                mais_gordo = [nome, peso]
            if peso < mais_magro[1]:
                mais_magro = [nome, peso]