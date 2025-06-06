'''
Descrição: Dada a lista numeros = [5, 10, 15, 20, 25]:
Altere o segundo elemento da lista para 12.
Some 5 ao último elemento da lista e atualize seu valor.
Imprima a lista modificada.
'''

numeros = [5, 10, 15, 20, 25]

for indice, numero in enumerate(numeros):
    if indice == 1:
        numeros[indice] = 12

numeros[-1] += 5

for numero in numeros:
    print(numero)