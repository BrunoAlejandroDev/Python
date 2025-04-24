'''
Escreva um programa que leia 15 números inteiros e, em seguida, exiba quantos desses números são positivos e quantos são negativos.
'''

def contador_positivo_negativo():
    #* Variaveis
    lista_numeros = [] # lista vazia para armazenar os valores do usuario
    contador_positivo = 0
    contador_negativo = 0

    #* Solicitar ao Usuario os Valores
    for i in range(1, 16):
        numeros = int(input(f'Digite o numero {i}: '))
        lista_numeros.append(numeros) # enviar a lista os valores inseridos pelo usuario

    contagem = [contador_positivo if num > 0 else contador_negativo for num in lista_numeros]