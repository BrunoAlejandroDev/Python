'''
Crie um dicionário com dados temporários e use .clear() para limpá-lo.
Verifique se ficou vazio com bool(dicionario).
'''

dicionario = {
    'bruno' : 24,
    'alicia' : 22,
    'pedro' : 12,
    'emma'  : 34,
    'luke' : 18,
    'mel' : 7
}

print('Antes da exclusao:')
for nome, idade in dicionario.items():
    print(f'Nome: {nome} - idade: {idade}')

print('\nLimpando o dicionario:')
dicionario.clear()
if bool(dicionario):
    print('Ainda tem itens')
else:
    print('todos os itens foram excluidos')