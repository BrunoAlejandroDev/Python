'''
Exercício 3: Métodos de Adição e Remoção

Descrição: Comece com uma lista vazia chamada convidados.
Adicione três nomes de convidados à lista usando o método append().
Insira um novo convidado na segunda posição da lista usando o método insert().
Remova o primeiro convidado da lista usando o método pop().
Remova um convidado específico pelo nome usando o método remove().
Imprima a lista final de convidados.
'''

nomes = ['Bruno', 'Alicia', 'Vojvoda', 'Taylor']
convidados = list(nomes) #* inicializa a lista com os valores da lista nome

for convidado in nomes:
    convidados.append(convidado) #* preenche a lista 

convidados.insert(1, 'Chico Moedas') #* insere um valor na lista em uma posicao especifica (retorna None)
print(f'Após inserir "Chico Moedas": {convidados}')

remover_primeiro = convidados.pop(0)
print(f'Convidado removido: {remover_primeiro}')
print(f'Apos remover o primeiro candidato: {convidados}')

convidados.remove('Vojvoda') #* remove um elemento especifico com base no seu valor (retorna None)
print(f'Apos remover "Vojvoda": {convidados}')

print(f'Lista final: {convidados}')