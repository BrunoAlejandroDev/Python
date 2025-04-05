"""
Desenvolva um programa que declare duas variáveis inteiras e realize as operações de 
soma, subtração, multiplicação, divisão e módulo entre elas. Exiba os resultados de cada 
operação
"""

def operacoes():
    numero1 = 12
    numero2 = 6

    soma = numero1 + numero2
    print(soma)

    subtracao = numero1 - numero2
    print(subtracao)

    multiplicacao = numero1 * numero2
    print(multiplicacao)

    # Divisao
    divisao = numero1 / numero2
    print(divisao)

    # Divisao inteira
    divisao_inteira = numero1 // numero2
    print(divisao_inteira)

    # Modulo
    modulo = numero1 % numero2
    print(modulo)

operacoes()