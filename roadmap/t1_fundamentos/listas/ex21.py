
#* Ordenação: Crie uma função ordenar_nomes(lista_nomes) que receba uma lista de strings desordenada e retorne a lista em ordem alfabética. (Pesquise sobre .sort() vs sorted()).


def ordenar_nomes(lista_nomes):
    return sorted(lista_nomes)

nomes = ['Vojvoda', 'Luffy', 'Lucca', 'Ademir', 'Britez', 'Bombom', 'Xixico', 'Micalateia']
print(ordenar_nomes(nomes))
print(nomes)