'''
Exercício 3: Métodos de Adição e Remoção

Descrição: Comece com uma lista vazia chamada convidados.
Adicione três nomes de convidados à lista usando o método append().
Insira um novo convidado na segunda posição da lista usando o método insert().
Remova o primeiro convidado da lista usando o método pop().
Remova um convidado específico pelo nome usando o método remove().
Imprima a lista final de convidados.
'''

convidados = []
nomes = ['Bruno', 'Alicia', 'Vojvoda', 'Taylor']


for convidado in nomes:
    convidados.append(convidado)

print('Inicial:')
for convidado in convidados:
    print(convidado)

inserir_segunda_posicao = convidados.insert(1, 'Chico Moedas')

remover_primeiro = convidados.pop(0)
print(f'Primeiro convidado removido: {remover_primeiro}')

remover_especifico = convidados.remove('Vojvoda')

print('Final:')
for convidado in convidados:
    print(convidado)