lista_convidados = ['Alicia', 'Souza', 'Leonardo']

#* Adicionar Novas Pessoas a Lista
lista_convidados.insert(0, 'Gilvan')
print(lista_convidados)

lista_convidados.insert(2, 'Daniel')
print(lista_convidados)

lista_convidados.append('Nelio')
print(lista_convidados)

#* Removendo Convidados com pop()
lista_convidados.pop()
print(lista_convidados)

lista_convidados.pop()
print(lista_convidados)

lista_convidados.pop()
print(lista_convidados)

lista_convidados.pop()
print(lista_convidados)

#* Remover Convidados com del
del lista_convidados[0]
print(lista_convidados)