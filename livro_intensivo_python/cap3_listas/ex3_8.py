'''
Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de visitar. Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
'''

lista_lugares = ['Italia', 'Canada', 'Uruguai', 'Gramado', 'Suecia']

#* ex1: Exiba sua lista na ordem original.
print(lista_lugares)
print()

#* Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita
print(f'lista ordenada: {sorted(lista_lugares)}')
print(f'lista original: {lista_lugares}\n')

#* Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.
print(f'Lista ordenada de forma inversa: {sorted(lista_lugares)}')
print(f'lista original: {lista_lugares}\n')