'''
Descrição: Crie uma função chamada maior_menor_valor que receba uma lista de números e retorne uma tupla contendo o maior e o menor valor encontrados na lista.
Exemplo: maior_menor_valor([5, 2, 8, 1, 9, 4]) deve retornar (9, 1).
Restrição: Não utilize as funções max() e min() prontas do Python. Implemente a lógica de comparação.
Desafio extra: Se a lista estiver vazia, a função deve retornar (None, None).
'''

def maior_menor_valor(lista_numeros):
    maior_menor = () #* tupla para receber o maior e o menor valor
    maior_valor = lista_numeros[0] # inicializa a variavel com o primeiro valor da lista para posterior comparacao
    menor_valor = lista_numeros[0] # inicializa a variavel com o primeiro valor da lista para posterior comparacao
    
    if len(lista_numeros) == 0:
        return maior_menor(None, None)
    else:
        for num in lista_numeros:
            if num > maior_valor:
                maior_valor = num
            elif num < menor_valor:
                menor_valor = num

    maior_menor = (maior_valor, menor_valor)
    return maior_menor
    
numeros = [5, 2, 8, 1, 9, 4]
maior_menor = maior_menor_valor(numeros)
print(maior_menor)