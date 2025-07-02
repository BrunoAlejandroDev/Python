'''
Data: 02/07/25
Enunciado: Escreva um programa que receba uma lista de números inteiros e retorne uma nova lista contendo apenas os números que são divisíveis por 3 E por 5 ao mesmo tempo.

Exemplo:
Entrada: [15, 3, 10, 30, 9, 45, 8]
Saída: [15, 30, 45]
'''

def verificar_multiplos(lista_numeros):
    lista_multiplos = []

    for numero in lista_numeros:
        if numero % 3 == 0 and numero % 5 == 0:
            lista_multiplos.append(numero)

    return lista_multiplos

lista_numeros = [15, 3, 10, 30, 9, 45, 8]
multiplos = verificar_multiplos(lista_numeros)
print(multiplos)