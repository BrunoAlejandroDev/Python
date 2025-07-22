'''
Exercício 2
Data: 22/07/2025

Enunciado: Escreva uma função que recebe uma lista de números inteiros e um número n. A função deve retornar a soma de todos os números da lista que são estritamente maiores que n.

Exemplo:
Entrada: lista = [10, 4, 8, 15, 7], n = 8
Saída: 25 (pois 10 + 15 = 25)

Habilidades desenvolvidas: Funções, manipulação de listas, laços de repetição, lógica condicional, operadores de comparação.
'''

def somar_numeros(lista_numeros, numero_limite):
    #* Variavel de soma
    somar = 0

    #* Iterar sobre cada numero 
    for numero in lista_numeros:
        #* Comparar o numero atual com o numero limite
        if numero > numero_limite:
            somar += numero

    return somar

lista = [10, 4, 8, 15, 7]
print(somar_numeros(lista, 8))