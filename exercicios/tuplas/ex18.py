'''
Crie uma lista de tuplas chamada pessoas, onde cada tupla tem (nome, idade).
a) Use um loop para imprimir: "{nome} tem {idade} anos" para cada pessoa.
'''

lista_pessoas = [('bruno', 24), ('alicia', 22), ('carlos', 33), ('bob esponja', 4)]

for nome, idade in lista_pessoas:
    print(f'{nome} tem {idade} anos')