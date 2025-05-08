'''
Some todos os valores do dicionário vendas = {"jan": 1000, "fev": 1200, "mar": 900} e imprima o total.
'''

dicionario = {
    'janeiro' : 1000,
    'fevereiro' : 1200,
    'marco' : 900
}
total = 0
for valor in dicionario.values():
    total += valor

print(total)