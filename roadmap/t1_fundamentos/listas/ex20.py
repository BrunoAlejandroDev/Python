
#* Remoção Segura (Try/Except): Crie uma função remover_item(lista, item). Ela deve tentar remover o item da lista usando .remove(). Se o item não existir, o Python geraria um ValueError. Capture esse erro com try/except e printe "Item não encontrado", mantendo a lista original.


def remover_item(lista, item):
    while True:
        try:
            if item in lista:
                lista.remove(item)
                print('Elemento removido com sucesso')
                break
        except ValueError:
            print('Item nao existe na lista')

lista = [1, 6, 8, 91, 20, 543, 43, 80]
print(f'Lista original: {lista}')

remover_item(lista, 81)

print(lista)