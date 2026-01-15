
#* Argumento Padrão: Crie uma função potencia(base, expoente=2). Se o usuário não mandar o expoente, ela deve elevar ao quadrado. Se mandar, eleva ao expoente informado.

import math

def potencia(base, expoente=2):
    '''
    Função que recebe dois parâmetros e retorna o primeiro parâmetro elevado o segundo.
    
    Args:
        base: valor inteiro
        expoente: valor inteiro

    Returns:
        Int: Valor da base elevado ao expoente
    '''

    return math.pow(base, expoente)

print(potencia(2, 9))