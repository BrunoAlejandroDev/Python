'''
Dada uma lista de números, substitua os números negativos por 0:
'''

numeros = [3, -1, 5, -9, 0, 7, 10, 6]
numeros_positivos = [num if num > 0 else 0 for num in numeros]
print(numeros_positivos)