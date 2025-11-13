'''
Exercício 2
Data: 23/07/2025

Enunciado: Escreva uma função que recebe um número inteiro positivo n e calcula a soma de todos os números pares de 1 até n (inclusive).

Exemplo:
Entrada: n = 10
Saída: 30 (pois 2 + 4 + 6 + 8 + 10 = 30)

Habilidades desenvolvidas: Laços de repetição (for com range), operadores matemáticos (módulo %), lógica condicional, acumulação de valores.
'''

def somar_pares(numero: int):

    #* Variavel para guardar o valor da soma
    somatorio = 0

    #* Verificar se o numero recebido é inteiro e positivo
    if not isinstance(numero, int) and numero < 0:
        print('O numero deve ser um valor inteiro positivo')
        return
    
    else:
        #* Percorrer cada numero da seguencia de 1 até o numero informado
        for numero in range(1, numero+1):
            #* Verificar se o numero atual da sequencia é par
            if numero % 2 == 0:
                #* Caso sim, somar o valor do numero com o valor da variavel somatório
                somatorio += numero

    return somatorio

numero = 10
print(somar_pares(numero))