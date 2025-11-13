'''
Crie uma tupla numeros com os valores (1, 2, 2, 3, 4, 2, 5).
a. conte quantas vezes o número 2 aparece na tupla numeros.
b. encontre o índice da primeira ocorrência do número 4 na tupla numeros.
'''

numeros = (1, 2, 2, 3, 4, 2, 5)

#* item a
quantidade_numero2 = numeros.count(2)
print(f'Quantidade de vezes que o numero 2 aparece: {quantidade_numero2}')

#* item b
primeiro_indice = numeros.index(4)
print(f'Primeiro indice valor 4: {primeiro_indice}')