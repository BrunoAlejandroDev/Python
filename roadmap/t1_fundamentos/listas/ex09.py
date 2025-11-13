'''
Descrição: Dada a lista numeros = [5, 10, 15, 20, 25]:
Altere o segundo elemento da lista para 12.
Some 5 ao último elemento da lista e atualize seu valor.
Imprima a lista modificada.
'''

numeros = [5, 10, 15, 20, 25]

numeros[1] = 12 #* alterar o segundo elemento
numeros[-1] += 5 #* somar 5 ao valor do ultimo elemento

for numero in numeros:
    print(numero)