'''
Crie uma tupla nomes com os valores ("Ana", "Beto", "Carlos", "Diana", "Eduarda").

a) Imprima os três primeiros nomes usando fatiamento.

b) Desempacote os dois últimos nomes da tupla em duas variáveis.

c) Use .index() para descobrir a posição do nome "Carlos".
'''

nomes = ('Ana', 'Beto', 'Carlos', 'Diana', 'Eduarda')

#* Item a: 
primeiros_nomes = nomes[:3]
print(primeiros_nomes)

#* Item b:
ultimos_nomes = nomes[3:]
nome1, nome2 = ultimos_nomes
print(f'nome 1: {nome1}\nnome 2: {nome2}')

#* item c:
posicao = nomes.index('Carlos')
print(f'Posicao: {posicao}')