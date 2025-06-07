'''
Descrição: Crie uma função chamada filtra_pares que receba uma lista de números inteiros e retorne uma nova lista contendo apenas os números pares da lista original. Se a lista original estiver vazia, retorne uma lista vazia.
Exemplo: filtra_pares([1, 2, 3, 4, 5, 6, 7, 8]) deve retornar [2, 4, 6, 8].
Dica: Use o operador módulo (%) para verificar se um número é par.
'''

def filtrar_pares(lista_numeros):
    lista_pares = [] #* lista para receber os numeros pares da lista passada como argumento
    
    for num in lista_numeros:
        if num % 2 == 0: #* verifica se o num atual do laço é par
            lista_pares.append(num)
            
    #? outra forma de fazer
    # pares = [num for num in lista_numeros if num % 2 == 0]
    # return pares
    
    return lista_pares

numeros = [1, 4, 2, 7, 9, 5, 6, 12, 11]
pares = filtrar_pares(numeros)
print(pares)