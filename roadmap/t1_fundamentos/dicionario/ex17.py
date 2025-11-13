'''
Data: 01/07/25
Exercício: Inversão de Dicionário
    Crie uma função chamada inverter_dicionario que recebe um dicionário como argumento. Supondo que os valores do dicionário também são únicos, a função deve retornar um novo dicionário onde as chaves se tornam valores e os valores se tornam chaves.
Exemplo: Se a entrada for {'a': 1, 'b': 2, 'c': 3}, o retorno deve ser {1: 'a', 2: 'b', 3: 'c'}.
Pense: O que aconteceria se os valores do dicionário original não fossem únicos? Como você poderia lidar com isso?
'''

dict_original = {
    'a' : 1,
    'b': 2,
    'c': 3
}

dict_novo = {}

for chave, valor in dict_original.items():
    nova_chave = valor
    novo_valor = chave

    if not nova_chave in dict_novo:
        dict_novo[nova_chave] = novo_valor
    else:
        dict_novo[nova_chave].append(novo_valor)

print(dict_novo)