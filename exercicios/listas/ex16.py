'''
Exercício 9: Contagem de Palavras com Mais de N Caracteres
    Descrição: Crie uma função chamada conta_palavras_longas que receba uma lista de palavras (strings) e um número inteiro n. A função deve retornar a quantidade de palavras na lista que possuem mais de n caracteres.
    Exemplo: conta_palavras_longas(["gato", "cachorro", "pássaro", "sol", "lua"], 4) deve retornar 2 (para "cachorro" e "pássaro").
'''

def contar_palavras_longas(lista_palavras, numero):
    contador = 0
    for palavra in lista_palavras:
        if len(palavra) > numero:
            contador += 1
            
    return contador

lista = ["gato", "cachorro", "pássaro", "sol", "lua"]
contador = contar_palavras_longas(lista, 4)
print(contador)