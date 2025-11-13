'''
Você tem um dicionário que representa o estoque de uma loja: estoque = {'tomate': 10, 'alface': 5, 'batata': 20, 'feijão': 15}.
Escreva um código que faça o seguinte:

Imprima todos os produtos (chaves) que têm um estoque maior que 10.
Peça ao usuário para digitar o nome de um produto e, caso o produto exista no dicionário, imprima a quantidade em estoque. Caso contrário, imprima "Produto não encontrado.".
Use um laço para imprimir a frase "Temos [quantidade] unidades de [produto]." para cada item no estoque.
'''

#* Criar dicionario
estoque = {
    'tomate' : 10,
    'alface' : 5,
    'batata' : 20,
    'feijao' : 15,
}

#* Imprimir todos produtos com mais de 10 unidades
produtos_com_mais_de_10_unidades = []
for produto, quantidade in estoque.items():
    if quantidade > 10:
        produtos_com_mais_de_10_unidades.append(produto)
print('Produtos com mais de 10 unidades:')
print(produtos_com_mais_de_10_unidades)

#* Encontrar produto no estoque
def encontrar_produto(produto, dicionario):
    if produto in dicionario:
        print(f'Nome do produto: {produto} | Quantidade em estoque: {dicionario.get(produto)}\n')
    else:
        print(f'Produto {produto} nao encontrado no estoque\n')

nome_produto = input('Digite o nome do produto: ')
encontrar_produto(nome_produto, estoque)

#* Imprimir estoque
def imprimir_estoque(dicionario):
    print('\n=== ESTOQUE ===')
    for produto, quantidade in dicionario.items():
        print(f'Temos {quantidade} unidade de {produto}')
imprimir_estoque(estoque)