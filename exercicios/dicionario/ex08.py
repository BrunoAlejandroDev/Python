'''
Crie um dicionário com 4 pares chave-valor (ex: frutas e preços).
a. Remova dois itens com del
b. Use .pop() para remover o terceiro
'''

frutas = {
    'banana' : 2.5,
    'caqui' : 3.75,
    'manga' : 5,
    'melao' : 10
}

print(f'Dicionario original: {frutas.items()}\n')

#* item a
del frutas['caqui']
del frutas['manga']
print(f'Remocao caqui e manga: {frutas.items()}\n')

#* item b
remover_fruta = frutas.pop('banana', 'Chave nao encontrada')
print(f'Fruta removida com pop: {remover_fruta}')