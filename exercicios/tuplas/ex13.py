'''
Crie uma função operacoes(a, b) que retorne (soma, subtração, multiplicação) dos dois valores.
a) Desempacote o retorno da função em três variáveis e imprima
'''

def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b

    return soma, subtracao, multiplicacao

print(operacoes(10, 4))