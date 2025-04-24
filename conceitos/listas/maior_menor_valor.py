
#* Lista com elementos de valores aleatorios
lista = [100, 1400, 1610, 202, 270, 1000]

#? Como pegar o menor valor da lista
menor_valor = min(lista)
print(menor_valor)

#? Como pegar o maior valor da lista
maior_valor = max(lista)
print(maior_valor)

#? Como descobrir os indices do menor valor e do maior valor
indice_menor_valor = lista.index(menor_valor)
print(f'Indice menor valor: {indice_menor_valor}')

indice_maior_valor = lista.index(maior_valor)
print(f'Indice menor valor: {indice_maior_valor}')