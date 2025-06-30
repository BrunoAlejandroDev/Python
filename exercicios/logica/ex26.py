'''
Data: 30/06/25
Exercício: Somatório com Critério
Enunciado: Escreva um programa que recebe uma lista de números inteiros e calcula a soma de todos os números que são maiores que 10.
Exemplo:
Entrada: [5, 12, 3, 20, 8, 15]
Saída: 47  (Explicação: 12 + 20 + 15)
'''

def somar_numeros_maiores(lista_numeros):
    #* Lista para colocar os numeros maiores que 10
    lista_maiores_que_10 = []

    #* Filtrar numeros maiores que 10
    for numero in lista_numeros:
        if numero > 10: # verifica se o numero atual é maior que 10
            lista_maiores_que_10.append(numero)

    somatorio = 0
    for numero in lista_maiores_que_10:
        somatorio += numero

    return somatorio

lista = [5, 12, 3, 20, 8, 15]
soma = somar_numeros_maiores(lista)
print(soma)