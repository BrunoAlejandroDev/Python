'''
Converta a tupla numeros = (1, 2, 3, 4) para lista e adicione o número 5.
a) Converta de volta para tupla e imprima.
'''

tupla_numeros = (1, 2, 3, 4)
tupla_para_lista = list(tupla_numeros) # conversao da lista
tupla_para_lista.append(5) # insercao de um novo valor
print(tupla_para_lista) # verificacao se o novo valor foi incluido
lista_para_tupla = tuple(tupla_para_lista)
print(lista_para_tupla)