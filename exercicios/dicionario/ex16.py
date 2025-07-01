'''
Data: 01/07/25
Exercício: Agrupando por Chave
Crie uma função chamada agrupar_por_inicial que recebe uma lista de nomes. A função deve retornar um dicionário onde as chaves são as letras iniciais dos nomes e os valores são listas com todos os nomes que começam com aquela letra.
Exemplo: Se a entrada for ['Ana', 'Beatriz', 'Bruno', 'Alice', 'Carlos'], o retorno deve ser {'A': ['Ana', 'Alice'], 'B': ['Beatriz', 'Bruno'], 'C': ['Carlos']}.
'''

lista_nomes = ['Ana', 'Beatriz', 'Bruno', 'Alicia', 'Carlos']
dicionario = {}

#* Iterar sobre cada nome da lista
for nome in lista_nomes: 
    #* Iterar sobre cada indice e cada letra de cada um dos nomes
    for indice, letra in enumerate(nome):
        if indice == 0: #* se o indice for zero significa que é a primeira letra do nome
            primeira_letra = letra #* Salvar a primeira letra em uma variavel
            if not primeira_letra in dicionario: #* Verificar se a letra existe no dicionario, se nao, adicionar ela e o valor
                dicionario[primeira_letra] = [nome]
            else: #* caso a letra ja esteja no dicionario, adicionar os novos valores que começam com a letra correspondente
                dicionario[primeira_letra].append(nome)

print(dicionario)