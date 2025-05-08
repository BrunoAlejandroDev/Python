'''
Remova a chave "ano"
Tente remover a chave "cor" com pop() e valor padrão "Não existe"
'''

carro = {
    'marca' : 'mercedes',
    'modelo' : 'amg',
    'ano' : '2025'
}
print(f'Dicionario original: {carro.items()}\n')

#* item a:
del carro['ano']
print(f'Exclusao do ano com del:\n{carro.items()}')

remover_cor = carro.pop('cor', 'Chave nao existe')
print(f'\nRemover chave cor: {remover_cor}')